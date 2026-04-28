from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from models import Base, Post, Comment
from pydantic import BaseModel

# 🔥 CREATE TABLES AUTOMATICALLY
Base.metadata.create_all(bind=engine)

app = FastAPI()

# ---------------- DB DEPENDENCY ----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- SCHEMAS ----------------
class PostCreate(BaseModel):
    email: str
    state: str
    district: str
    message: str

class CommentCreate(BaseModel):
    email: str
    text: str

# ---------------- TRUST LOGIC ----------------
def trust_status(post: Post):
    if post.likes - post.dislikes >= 5:
        return "TRUSTED"
    if post.dislikes - post.likes >= 5:
        return "FAKE"
    return "UNVERIFIED"

# ---------------- ROUTES ----------------

@app.post("/posts")
def create_post(data: PostCreate, db: Session = Depends(get_db)):
    post = Post(
        email=data.email,
        state=data.state,
        district=data.district,
        message=data.message
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return {"status": "ok", "post_id": post.id}


@app.get("/posts")
def get_posts(state: str, db: Session = Depends(get_db)):
    posts = db.query(Post).filter(Post.state == state).all()

    result = []
    for p in posts:
        result.append({
            "id": p.id,
            "email": p.email,
            "state": p.state,
            "district": p.district,
            "message": p.message,
            "likes": p.likes,
            "dislikes": p.dislikes,
            "trust_status": trust_status(p),
            "comments": [
                {"email": c.email, "text": c.text}
                for c in p.comments
            ]
        })
    return result


@app.post("/posts/{post_id}/like")
def like_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).get(post_id)
    if post:
        post.likes += 1
        db.commit()
    return {"status": "liked"}


@app.post("/posts/{post_id}/dislike")
def dislike_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).get(post_id)
    if post:
        post.dislikes += 1
        db.commit()
    return {"status": "disliked"}


@app.post("/posts/{post_id}/comment")
def add_comment(post_id: int, data: CommentCreate, db: Session = Depends(get_db)):
    comment = Comment(
        post_id=post_id,
        email=data.email,
        text=data.text
    )
    db.add(comment)
    db.commit()
    return {"status": "comment added"}

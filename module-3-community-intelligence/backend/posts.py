from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Post, Comment
import shutil, os

router = APIRouter()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create-post")
def create_post(
    user_id: int,
    description: str,
    state: str,
    district: str,
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    file_path = f"{UPLOAD_DIR}/{image.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    post = Post(
        user_id=user_id,
        description=description,
        image=file_path,
        state=state,
        district=district
    )
    db.add(post)
    db.commit()
    return {"message": "Post created"}

@router.get("/posts")
def get_posts(state: str = None, district: str = None, db: Session = Depends(get_db)):
    query = db.query(Post)
    if state:
        query = query.filter(Post.state == state)
    if district:
        query = query.filter(Post.district == district)
    return query.order_by(Post.created_at.desc()).all()

@router.post("/like/{post_id}")
def like_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).get(post_id)
    post.likes += 1
    db.commit()
    return {"likes": post.likes}

@router.post("/dislike/{post_id}")
def dislike_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).get(post_id)
    post.dislikes += 1
    db.commit()
    return {"dislikes": post.dislikes}

@router.post("/comment")
def comment(post_id: int, user: str, text: str, db: Session = Depends(get_db)):
    c = Comment(post_id=post_id, user=user, text=text)
    db.add(c)
    db.commit()
    return {"message": "Comment added"}

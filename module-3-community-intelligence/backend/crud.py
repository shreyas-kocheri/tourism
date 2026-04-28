from sqlalchemy.orm import Session
from models import Post, Comment

def create_post(db: Session, data):
    post = Post(
        email=data.email,
        state=data.state,
        district=data.district,
        message=data.message
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_posts(db: Session, state: str = None):
    q = db.query(Post)
    if state:
        q = q.filter(Post.state == state)
    return q.all()

def like_post(db: Session, post_id: int):
    post = db.query(Post).get(post_id)
    post.likes += 1
    db.commit()
    return post

def dislike_post(db: Session, post_id: int):
    post = db.query(Post).get(post_id)
    post.dislikes += 1
    db.commit()
    return post

def add_comment(db: Session, post_id: int, email: str, text: str):
    comment = Comment(
        post_id=post_id,
        email=email,
        text=text
    )
    db.add(comment)
    db.commit()
    return comment

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    state = Column(String, index=True)
    district = Column(String)
    message = Column(String)

    likes = Column(Integer, default=0)
    dislikes = Column(Integer, default=0)

    comments = relationship("Comment", back_populates="post", cascade="all, delete")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    email = Column(String)
    text = Column(String)

    post = relationship("Post", back_populates="comments")

from sqlalchemy.orm import Session
from .models import Post, User

def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Post).offset(skip).limit(limit).all()

def create_post(db: Session, post: Post):
    db.add(post)
    db.commit()
    db.refresh(post)

def get_post_by_id(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

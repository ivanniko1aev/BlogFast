from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session, Depends
from utils.html import templates
from crud import get_posts, create_post, get_post_by_id, get_users, create_user, get_user_by_username
from database import SessionLocal

router = APIRouter(
    prefix="/blog",
    tags=["blog"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_class=HTMLResponse)
async def blog_home(request: Request, db: Session = Depends(get_db)):
    posts = get_posts(db)
    context = {"request": request, "posts": posts}
    return templates.TemplateResponse("blog/index.html", context)

@router.get("/edit", response_class=HTMLResponse)
async def blog_edit(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("blog/edit.html", context)

@router.get("/edit/{blog_id}", response_class=HTMLResponse)
async def blog_edit_id(request: Request, blog_id: int):
    context = {
        "request": request,
        "blog_id": blog_id
            }
    return templates.TemplateResponse("blog/index.html", context)


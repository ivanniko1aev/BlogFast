from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from utils.html import templates

router = APIRouter(
    prefix="/blog",
    tags=["blog"],
)

@router.get("/", response_class=HTMLResponse)
async def blog_home(request: Request):
    context = {"request": request}
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


from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ..utils.blog import get_blog_posts

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def blog(request: Request):
    blog_posts = get_blog_posts()
    return templates.TemplateResponse("blog.html", {"request": request, "blog_posts": blog_posts})
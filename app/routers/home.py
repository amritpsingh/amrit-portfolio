from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import yaml
from data.services import services
from data.skills import skills
from data.testimonials import testimonials

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def load_yaml_data(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    services_bg_url = request.url_for('static', path='/images/Orange-Yellow-Gradient-3.png')
    
    # Load blog data
    blogs = load_yaml_data('content/_blogs.yml')
    
    # Load project data
    projects = load_yaml_data('content/_projects.yml')




    return templates.TemplateResponse("home.html", {
        "request": request,
        "services_bg_url": services_bg_url,
        "services": services,
        "skills": skills,
        "projects": projects,
        "blog_posts": blogs[:3],  # Display only the latest 3 posts
        "testimonials": testimonials
    })
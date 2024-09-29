from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import yaml

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def load_yaml_data(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
    

@router.get("/", response_class=HTMLResponse)
async def projects(request: Request):

    # Load project data
    projects = load_yaml_data('content/_projects.yml')

    return templates.TemplateResponse("projects.html", {
        "request": request,
        "projects": projects
        })
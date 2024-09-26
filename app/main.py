from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import home, about, blog, projects, contact

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(home.router, prefix="", tags=["home"])
app.include_router(about.router, prefix="/about", tags=["about"])
app.include_router(blog.router, prefix="/blog", tags=["blog"])
app.include_router(projects.router, prefix="/projects", tags=["projects"])
app.include_router(contact.router, prefix="/contact", tags=["contact"])

@app.get("/", name="home")
async def root():
    return {"message": "Welcome to my portfolio website!"}
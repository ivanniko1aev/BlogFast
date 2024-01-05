from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from utils.html import mount_static
from routers import blog


app = FastAPI()

app.include_router(blog.router)
mount_static()
from exceptions import handler




from fastapi import Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jinja2.exceptions import TemplateNotFound 
from logging import getLogger
import main 
log = getLogger("general")


def mount_static():
    main.app.mount("/static", StaticFiles(directory="static"), name="static")

class CustomJinja2Templates(Jinja2Templates):
    def __init__(self, directory: str):
        super().__init__(directory=directory)
        
    def get_template(self, name: str):
        try:
            return self.env.get_template(name)
        except TemplateNotFound:
            log.warning(f"Template not found: {name}") 
            raise HTTPException(status_code=404, detail="Template not found")
        
         
templates = CustomJinja2Templates(directory="templates")

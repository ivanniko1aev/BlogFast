from fastapi import Request, Response
from starlette.exceptions import HTTPException as StarletteHTTPException
from utils.html import templates
from main import app


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc) -> Response:
    context = {
        "request": request, 
        "status_code": exc.status_code,
        "detail": exc.detail }
    return templates.TemplateResponse("exceptions/http_exception.html", context) 
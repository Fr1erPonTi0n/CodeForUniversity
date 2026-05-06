from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from datetime import date

from core.config import BASE_DIR
from templating.jinja_template import templates

router = APIRouter()

@router.get('/',
            response_class=HTMLResponse,
            include_in_schema=False,
            name='home',
            )
def read_root(
    request: Request,
) -> HTMLResponse:
    context = {}
    features = [
        'Create books',
        'Real time statistics',
        'Management',
    ]
    context.update(
        features=features,
    )
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context=context,
    )

@router.get('/about/',
            response_class=HTMLResponse,
            include_in_schema=False,
            name='about',
            )
def about_page(
    request: Request,
) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="about.html",
    )
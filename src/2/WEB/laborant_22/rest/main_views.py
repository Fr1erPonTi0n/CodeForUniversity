from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from templating.jinja_template import templates

router = APIRouter()

@router.get('/',
            response_class=HTMLResponse,
            name='home',
            )
def home_page(
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
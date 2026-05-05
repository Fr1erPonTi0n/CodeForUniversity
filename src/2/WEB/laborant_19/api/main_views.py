from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from datetime import date

from core.config import BASE_DIR
from templating.jinja_template import templates

router = APIRouter()

@router.get('/',
            response_class=HTMLResponse,
            include_in_schema=False,
            )
def read_root(
    request: Request,
) -> HTMLResponse:
    context = {}
    year = date.today().year
    features = [
        'Create books',
        'Real time statistics',
        'Management',
    ]
    context.update(
        year=year,
        features=features,
    )
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context=context
    )
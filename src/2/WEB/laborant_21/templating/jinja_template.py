from fastapi.templating import Jinja2Templates
from core.config import BASE_DIR

from datetime import date, datetime
from fastapi.requests import Request

def inject_current_year(
        request: Request,
) -> dict[str, date]:
    return {
        'year': date.today().year,
    }

templates = Jinja2Templates(
    directory=BASE_DIR / 'templates',
    context_processors=[
        inject_current_year,
    ],
)
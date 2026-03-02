from fastapi import (
    HTTPException,
    status,
    Depends,
    Request,
    # Query,
    # Header,
)
from core import (
    API_TOKENS,
    USERS_DB,
)
from typing import Annotated
from .crud import storage
from schemas import Book
from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials,
    HTTPBasic,
    HTTPBasicCredentials,
)

UNSAFE_METHODS = frozenset({
    "PATCH",
    "POST",
    "PUT",
    "DELETE",
})

api_token = HTTPBearer(
    scheme_name='API token',
    description='Enter your API token',
    auto_error=False,
)

user_auth = HTTPBasic(
    scheme_name='User Authetication',
    description='Enter your username and password',
    auto_error=False,

)

def prefetch_book(slug: str) -> Book:
    book = storage.get_by_slug(slug)
    if book:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Книга с slug '{slug}' не найдена",
    )

def api_token_required(
        request: Request,
        api_token: Annotated[
            HTTPAuthorizationCredentials | None,
            Depends(api_token),
        ] = "",
):
    if request.method not in UNSAFE_METHODS:
        return

    if not api_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API token is required",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if api_token.credentials not in API_TOKENS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API token",
            headers={"WWW-Authenticate": "Bearer"},
        )

def basic_user_auth(
        request: Request,
        credentials: Annotated[
            HTTPBasicCredentials | None,
            Depends(user_auth),
        ] = "",
):
    if request.method not in UNSAFE_METHODS:
        return

    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    if (
        credentials
        and credentials.username in USERS_DB
        and credentials.password == USERS_DB[credentials.username]
    ):
        return

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Basic"},
    )


BookDep = Annotated[Book, Depends(prefetch_book)]

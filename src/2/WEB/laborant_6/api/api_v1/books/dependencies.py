from fastapi import HTTPException, status, Depends, Request, Query, Header
from core import API_TOKENS
from typing import Annotated
from .crud import storage
from schemas import Book

UNSAFE_METHODS = frozenset({
    "PATCH",
    "POST",
    "PUT",
    "DELETE"
})

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
      str,
      Header()
  ] = "",
):
    if request.method not in UNSAFE_METHODS:
        return
    
    if api_token not in API_TOKENS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API token"
        )
    
BookDep = Annotated[Book, Depends(prefetch_book)]
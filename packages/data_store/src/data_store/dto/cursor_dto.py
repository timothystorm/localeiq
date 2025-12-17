from typing import TypeVar, Generic, Optional

from pydantic import BaseModel

# Generic type variable for response data
T = TypeVar("T")


class Cursor(BaseModel):
    """
    Pagination cursor metadata.
    """

    limit: Optional[int] = None
    after: Optional[str] = None


class CursorDto(BaseModel, Generic[T]):
    """
    Paginated response wrapper.
    """

    next: Optional[str] = None
    data: T

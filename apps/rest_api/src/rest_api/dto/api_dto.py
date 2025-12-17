from typing import List, Any, Dict, TypeVar, Generic, TypedDict, NotRequired

from pydantic import BaseModel

# Generic type variable for response data
T = TypeVar("T")


class Page(TypedDict):
    size: NotRequired[int | None]
    cursor: NotRequired[str | None]


class Meta(TypedDict):
    """
    Base metadata for API responses.
    - page: Optional pagination metadata.
    - query: Optional dictionary of input parameters used in the request.
    - warnings: Optional list of warning messages.
    """

    page: NotRequired[Page]
    query: NotRequired[Dict[str, Any]]
    warnings: NotRequired[List[str]]


class StandardResponse(BaseModel, Generic[T]):
    """
    Standard API response wrapper.

    - meta: Metadata about the response.
    - data: The actual response data of generic type T.
    """

    meta: Meta
    data: T

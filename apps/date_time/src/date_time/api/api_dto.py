from typing import Optional, List, Any, Dict, TypeVar, Generic

from pydantic import BaseModel

# Generic type variable for response data
T = TypeVar("T")


class Meta(BaseModel):
    """
    Base metadata for API responses.

    - input_params: Optional dictionary of input parameters used in the request.
    - warnings: Optional list of warning messages.
    """

    input_params: Optional[Dict[str, Any]]
    warnings: Optional[List[str]] = None


class StandardResponse(BaseModel, Generic[T]):
    """
    Standard API response wrapper.
    - meta: Metadata about the response.
    - data: The actual response data of generic type T.
    """

    meta: Meta
    data: T

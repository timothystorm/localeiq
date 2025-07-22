from typing import Optional

from pydantic import BaseModel


class TimeZone(BaseModel):
    utc_offset: str  # e.g., "+00:00", "-07:00"
    iana: str  # e.g., "America/Denver"
    std_abbreviation: str  # e.g., "MST"
    dst_abbreviation: Optional[str] = None  # e.g., "MDT" if applicable

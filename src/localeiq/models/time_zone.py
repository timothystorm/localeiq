from typing import Optional

from pydantic import BaseModel


class TimeZone(BaseModel):
    """
    Represents time zone information for a geographic region.

    Attributes:
       utc_offset (str): The UTC offset in the format ±HH:MM (e.g., "-07:00").
       iana (str): The IANA time zone name (e.g., "America/Denver").
       std_abbr (str): Abbreviation used during standard time (e.g., "MST").
       dst_abbr (Optional[str]): Abbreviation used during daylight saving time,
        if applicable (e.g., "MDT").
    """

    utc_offset: str
    iana: str
    std_abbr: str
    dst_abbr: Optional[str] = None

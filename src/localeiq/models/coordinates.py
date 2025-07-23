from pydantic import BaseModel


class Coordinates(BaseModel):
    """
    Represents the geographic coordinates of a location.

    Attributes:
        latitude (float): The latitude in decimal degrees (e.g., 39.7392).
        longitude (float): The longitude in decimal degrees (e.g., -104.9903).
    """

    latitude: float
    longitude: float

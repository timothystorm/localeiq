from typing import Optional, Union, List

from localeiq.models.region import Region
from localeiq.repository.region_repository import RegionRepository


class RegionService:
    """
    Service managing regions-related operations.
    """

    def __init__(self):
        """
        Initializes the region service with a repository instance.
        """
        self._repository = RegionRepository()

    def get_region_by_country_postal(
        self, country: str, postal: str
    ) -> Optional[Region]:
        matches = self._repository.find_by_country_and_postal(country, postal)
        return matches[0] if matches else None

    def get_region_by_postal(self, postal: str) -> Union[Region, List[Region], None]:
        matches = self._repository.find_by_postal(postal)
        if not matches:
            return None
        if len(matches) == 1:
            return matches[0]
        return matches

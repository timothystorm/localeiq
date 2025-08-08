from typing import List

from localeiq.models.country import Country
from localeiq.repository.countries_repository import CountriesRepository


class CountryService:
    """
    Service for managing country-related operations.
    """

    def __init__(self):
        self._repository = CountriesRepository()

    def get_country_list(self, locale: str) -> List[Country]:
        """
        Returns a list of all countries.
        """
        parts = locale.replace("_", "-").split("-")
        iso_locale = (
            f"{parts[0].lower()}-{parts[1].upper()}"
            if len(parts) > 1
            else parts[0].lower()
        )
        return self._repository.all(iso_locale)

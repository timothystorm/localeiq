from typing import List

from localeiq.models.country import Country
from localeiq.repository.countries_repository import CountriesRepository


class CountryService:
    """
    Service for managing country-related operations.
    """

    def __init__(self):
        self._repository = CountriesRepository()

    def get_country_list(self) -> List[Country]:
        """
        Returns a list of all countries.
        """
        return self._repository.all()

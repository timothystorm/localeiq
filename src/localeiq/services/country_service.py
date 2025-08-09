from typing import List

from localeiq.models.country import Country
from localeiq.repository.country_repository import CountriesRepository


class CountryService:
    """
    Service for managing country-related operations.
    """

    def __init__(self, repo: CountriesRepository):
        self._repo = repo

    async def get_country_list(self, language_code: str = "en") -> List[Country]:
        """
        Returns a list of all countries.
        :param language_code: The language of the returned country names.
            The language must be a base language code and an optional country code. Default is 'en'.
            It can be a full language code (e.g., 'en-US', 'fr_CA', 'jp-jp', 'RU-RU')
            or a base language code (e.g., 'en', 'AR').
        :return: A list of Country with country names in the specified language.
        """
        parts = language_code.replace("_", "-").split("-")
        iso_language_code = (
            f"{parts[0].lower()}-{parts[1].upper()}"
            if len(parts) > 1
            else parts[0].lower()
        )
        return await self._repo.all(iso_language_code)

from contextlib import asynccontextmanager

from localeiq.db.session import db_session
from localeiq.repository.country_repository import CountriesRepository
from localeiq.services.country_service import CountryService


@asynccontextmanager
async def get_country_service():
    """
    Factory function to create an instance of CountryService.
    :return: An instance of CountryService.
    """
    async with db_session() as session:
        repo = CountriesRepository(session)
        service = CountryService(repo)
        yield service

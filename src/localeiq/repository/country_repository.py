from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from localeiq.db.schema import Country as CountrySchema
from localeiq.db.schema.country import CountryLocalizedName
from localeiq.models.country import Country as CountryModel


def _to_country_model(
    country_schema: CountrySchema, localized_name: Optional[str] = None
) -> CountryModel:
    """
    Converts a CountrySchema to a CountryModel.
    :param country_schema: The country schema instance from the database.
    :param localized_name: The localized name of the country.
    :return: A CountryModel instance with the country code and localized name.
    """
    return CountryModel(code=country_schema.iso_alpha2, name=localized_name or "")


class CountriesRepository:
    """
    A repository for managing country data.
    """

    def __init__(self, session: AsyncSession):
        self._session = session

    async def all(self, language_code: str) -> List[CountryModel]:
        """
        Returns a list of all countries in the specified language(s).
        :param language_code: The language of the returned country names.
            The language must be a valid ISO 639-1 language code and an optional ISO 3166-1 alpha-2 country code.
            It can be a full language code (e.g., 'en-US') or a base language code (e.g., 'en').
        :return: A list of CountryModel with country names in the specified language.
        """

        # Split the language code to handle both full and base language codes
        # e.g., 'en-US' will be split into 'en-US' and 'en'
        language_list = {language_code, language_code.split("-")[0].lower()}
        stmt = select(CountrySchema, CountryLocalizedName.localized_name).join(
            CountryLocalizedName,
            (CountryLocalizedName.country_id == CountrySchema.id)
            & (CountryLocalizedName.language_code.in_(language_list)),
        )

        results = await self._session.execute(stmt)
        rows = results.all()
        return [
            _to_country_model(country, localized_name=name) for country, name in rows
        ]

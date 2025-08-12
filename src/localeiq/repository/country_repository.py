from typing import List, Optional

from sqlalchemy import select, case
from sqlalchemy.ext.asyncio import AsyncSession

from localeiq.db.schema import CountrySchema, CountryLocalizedNameSchema
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
        language_base = language_code.split("-")[0].lower()
        candidates = {language_code, language_base}

        # Create a case expression to rank the localized names
        # preferring the full language code first, then the base language code
        rank_expr = case(
            (CountryLocalizedNameSchema.language_code == language_code, 1),
            (CountryLocalizedNameSchema.language_code == language_base, 1),
            else_=99,
        )

        stmt = (
            select(CountrySchema, CountryLocalizedNameSchema.localized_name)
            .join(
                CountryLocalizedNameSchema,
                CountryLocalizedNameSchema.country_id == CountrySchema.id,
            )
            .where(CountryLocalizedNameSchema.language_code.in_(candidates))
            .distinct(CountrySchema.id)
            # order_by is critical to pick the best localized name based on the rank
            .order_by(CountrySchema.id, rank_expr)
        )

        results = await self._session.execute(stmt)
        return [
            _to_country_model(country, localized_name=name)
            for country, name in results.all()
        ]

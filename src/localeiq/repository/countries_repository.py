from typing import List, Optional

from localeiq.db.schema import Country as CountrySchema
from localeiq.db.schema.country import CountryLocalizedName
from localeiq.db.session import SessionLocal
from localeiq.models.country import Country as CountryModel


def _to_country_model(
    country_schema: CountrySchema, localized_name: Optional[str] = None
) -> CountryModel:
    """
    Converts a country schema to a domain model.
    :param country_schema: The country schema instance from the database.
    :param localized_name: The localized name of the country.
    :return: A CountryModel instance with the country code and localized name.
    """
    return CountryModel(code=country_schema.iso_alpha2, name=localized_name or "")


class CountriesRepository:
    """
    A repository for managing country data.
    """

    def __init__(self):
        self._db = SessionLocal()

    def all(self, locale: str = "en") -> List[CountryModel]:
        """
        Returns a list of all countries for a locale
        :param locale: The locale to filter country names by.
            If no locale is provided, defaults to 'en'.
            If given, the locale must be a valid ISO 639-1 language code
                - ex. 'en-US', 'fr-CA', 'fr', 'zh-HANS'
        :return: A list of CountryModel instances with localized names.
        """
        locale_list = {locale, locale.split("-")[0].lower()}
        query = (
            self._db.query(CountrySchema)
            .join(
                CountryLocalizedName,
                (CountryLocalizedName.country_id == CountrySchema.id)
                & (CountryLocalizedName.language_code.in_(locale_list)),
            )
            .add_columns(CountryLocalizedName.localized_name)
        )

        results = query.all()

        return [
            _to_country_model(country_row, localized_name=localized_name)
            for country_row, localized_name in results
        ]

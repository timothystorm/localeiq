from typing import Sequence, Optional

from data_store.dto.locale_dto import LocaleDto, LocaleFilter
from data_store.repository.locale_repo import LocaleRepo


class LocaleService:
    """
    Service for handling locale-related operations and business logic.
    """

    def __init__(self, repo: LocaleRepo):
        self._repo = repo

    def get_locales(self, filters: Optional[LocaleFilter]) -> Sequence[LocaleDto]:
        """
        :param filters: optional filters to apply when retrieving locales.
        :return: list of locales matching the given language, or all locales if no language is specified.
        """
        return self._repo.read_locale(filters)

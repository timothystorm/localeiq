from typing import Sequence

from data_store.dto.locale_dto import LocaleDto
from data_store.repository.locale_repo import LocaleRepo


class LocaleService:
    """
    Service for handling locale-related operations and business logic.
    """

    def __init__(self, repo: LocaleRepo):
        self._repo = repo

    def get_locales(self, language: str | None = None) -> Sequence[LocaleDto]:
        """
        :param language: optional language tag to filter locales by. Ex. en, fr, de, etc.
        :return: list of locales matching the given language, or all locales if no language is specified.
        """
        if language:
            return self._repo.read_by_language(language)
        return self._repo.read_all()

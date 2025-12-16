from abc import ABC, abstractmethod
from typing import Sequence, Optional

from data_store.dto.locale_dto import LocaleDto, LocaleFilter


class LocaleRepo(ABC):
    """
    Abstract repository interface for locale data.
    """

    @abstractmethod
    def read_locale(
        self, filters: Optional[LocaleFilter] = None
    ) -> Sequence[LocaleDto]:
        """
        :return: list of locales for the given language, ordered by tag and optionally filtered
        """
        ...

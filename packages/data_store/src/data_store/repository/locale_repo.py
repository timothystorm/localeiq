from abc import ABC, abstractmethod
from typing import Sequence, Optional

from data_store.dto.cursor_dto import CursorDto, Cursor
from data_store.dto.locale_dto import LocaleDto, LocaleFilter


class LocaleRepo(ABC):
    """
    Abstract repository interface for locale data.
    """

    @abstractmethod
    def read_locale(
        self, *, filters: LocaleFilter, cursor: Optional[Cursor] = None
    ) -> CursorDto[Sequence[LocaleDto]]:
        """
        :param filters: optional filters to apply when retrieving locales
        :param cursor: optional cursor for pagination
        :return: cursored response of locales matching any given filters
        """
        ...

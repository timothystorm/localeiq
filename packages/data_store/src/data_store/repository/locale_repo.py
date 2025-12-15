from abc import ABC, abstractmethod
from typing import Sequence

from data_store.dto.locale_dto import LocaleDto


class LocaleRepo(ABC):
    @abstractmethod
    def read_all(self) -> Sequence[LocaleDto]:
        """
        :return: list of all locales in the datastore, ordered by tag
        """
        ...

    @abstractmethod
    def read_by_language(self, language: str) -> Sequence[LocaleDto]:
        """
        :return: list of locales for the given language, ordered by tag
        """
        ...

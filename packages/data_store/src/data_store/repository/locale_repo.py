from abc import ABC, abstractmethod

from data_store.dto.locale_dto import LocaleDto


class LocaleRepo(ABC):
    @abstractmethod
    def read_all(self) -> list[LocaleDto]:
        """
        :return: all locales from the datastore.
        """
        ...

    @abstractmethod
    def read_by_language(self, language: str) -> list[LocaleDto]: ...

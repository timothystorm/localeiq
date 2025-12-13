from abc import ABC, abstractmethod
from typing import Sequence

from data_store.dto.locale_dto import LocaleDto


class LocaleRepo(ABC):
    @abstractmethod
    def read_all(self) -> Sequence[LocaleDto]:
        """
        :return: all locales from the datastore.
        """
        ...

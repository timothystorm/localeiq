from abc import ABC, abstractmethod
from typing import Sequence

from data_store.dto.language_dto import LanguageDto


class LanguageRepo(ABC):
    @abstractmethod
    def read_all(self) -> Sequence[LanguageDto]:
        """
        Get all languages from the datastore.
        :return: all
        """
        ...

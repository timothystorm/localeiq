from data_store.dto.locale_dto import LocaleDto
from data_store.impl.locale_repo_impl import LocaleRepoImpl


class LocaleService:
    @staticmethod
    def get_locales(language: str | None = None) -> list[LocaleDto]:
        print(language)
        if language:
            return LocaleRepoImpl().read_by_language(language)
        return LocaleRepoImpl().read_all()

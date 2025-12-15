from data_store.impl.locale_repo_impl import LocaleRepoImpl
from data_store.repository.locale_repo import LocaleRepo


def get_locale_repository() -> LocaleRepo:
    """
    :return: An instance of LocaleRepo
    """
    return LocaleRepoImpl()

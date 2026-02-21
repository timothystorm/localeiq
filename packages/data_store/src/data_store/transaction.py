from contextlib import contextmanager

from data_store.engine import get_db_session
from data_store.settings import get_settings


@contextmanager
def read_only_session():
    """
    Legacy context manager for read-only operations.
    Note: This still commits, which is safe for read operations but misleading.
    Consider using get_db_session() dependency injection instead.
    """
    gen = get_db_session(get_settings())
    session = next(gen)
    try:
        yield session
        next(gen, None)
    except Exception:
        gen.throw(*__import__("sys").exc_info())
        raise

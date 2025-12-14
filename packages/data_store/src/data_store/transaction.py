from contextlib import contextmanager

from data_store.engine import SessionLocal


@contextmanager
def read_only_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

from pydantic import ValidationError
from shared.configuration import Configuration


def test_load_default():
    try:
        Configuration()
    except ValidationError:
        assert False, "Loading default configuration should not raise an error"

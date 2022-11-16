import pytest

from smdebug_rulesconfig.actions.utils import validate_email_address


@pytest.fixture
def key():
    return "email_address"


def test_validate_email_address(key):
    """
    Validates correct and incorrect email addresses passed to `validate_email_address` function.
    """
    with pytest.raises(ValueError):
        validate_email_address(key, 123)

    with pytest.raises(ValueError):
        validate_email_address(key, "abc@abc")

    assert validate_email_address(key, "abc@abc.com") is None

    assert validate_email_address(key, "abc@abc.def.com") is None

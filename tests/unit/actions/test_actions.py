from smdebug_rulesconfig import ActionList, StopTraining, Email, SMS, is_valid_action_object
import pytest


from tests.unit.actions.utils import validate_action_str


@pytest.fixture
def stop_training_name():
    return StopTraining.__name__.lower()


@pytest.fixture
def email_name():
    return Email.__name__.lower()


@pytest.fixture
def sms_name():
    return SMS.__name__.lower()


@pytest.fixture
def training_job_prefix():
    return "training-job-prefix"


@pytest.fixture
def training_job_name():
    return "training-job-name"


@pytest.fixture
def email_address():
    return "abc@abc.com"


@pytest.fixture
def phone_number():
    return "+1234567890"


def test_default_stop_training_action(stop_training_name, training_job_name):
    action = StopTraining()
    assert is_valid_action_object(action)
    validate_action_str(action.serialize(), action.action_parameters)
    assert action.use_default_training_job_prefix is True
    assert action.action_parameters == {"name": stop_training_name}

    action.update_training_job_prefix_if_not_specified(training_job_name)
    assert action.action_parameters == {
        "name": stop_training_name,
        "training_job_prefix": training_job_name,
    }


def test_custom_stop_training_action(stop_training_name, training_job_prefix, training_job_name):
    action = StopTraining(training_job_prefix)
    assert is_valid_action_object(action)
    validate_action_str(action.serialize(), action.action_parameters)
    assert action.use_default_training_job_prefix is False
    assert action.action_parameters == {
        "name": stop_training_name,
        "training_job_prefix": training_job_prefix,
    }

    action.update_training_job_prefix_if_not_specified(training_job_name)
    assert action.action_parameters == {
        "name": stop_training_name,
        "training_job_prefix": training_job_prefix,
    }


def test_email_action(email_name, email_address):
    action = Email(email_address)
    assert is_valid_action_object(action)
    validate_action_str(action.serialize(), action.action_parameters)
    assert action.action_parameters == {"name": email_name, "endpoint": email_address}


def test_sms_action(sms_name, phone_number):
    action = SMS(phone_number)
    assert is_valid_action_object(action)
    validate_action_str(action.serialize(), action.action_parameters)
    assert action.action_parameters == {"name": sms_name, "endpoint": phone_number}


def test_action_list(
    stop_training_name, email_name, sms_name, training_job_name, email_address, phone_number
):
    actions = ActionList(StopTraining(), Email(email_address), SMS(phone_number))
    assert is_valid_action_object(actions)
    action_parameters = [action.action_parameters for action in actions.actions]
    validate_action_str(actions.serialize(), action_parameters)
    assert action_parameters == [
        {"name": stop_training_name},
        {"name": email_name, "endpoint": email_address},
        {"name": sms_name, "endpoint": phone_number},
    ]

    actions.update_training_job_prefix_if_not_specified(training_job_name)
    assert action_parameters == [
        {"name": stop_training_name, "training_job_prefix": training_job_name},
        {"name": email_name, "endpoint": email_address},
        {"name": sms_name, "endpoint": phone_number},
    ]


def test_action_validation():
    with pytest.raises(AssertionError):
        StopTraining(10)

    with pytest.raises(AssertionError):
        Email(None)

    with pytest.raises(AssertionError):
        SMS(None)

    with pytest.raises(AssertionError):
        ActionList(StopTraining(), "bad_action")

    assert not is_valid_action_object("bad_action")

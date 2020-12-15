class Action(object):
    def __init__(self, training_job_prefix=None, **action_parameters):
        action_parameters["name"] = self.__class__.__name__.lower()

        if training_job_prefix is not None:
            action_parameters["training_job_prefix"] = training_job_prefix

        self.action_parameters = action_parameters

    def update_training_job_prefix(self, training_job_name):
        self.action_parameters["training_job_prefix"] = training_job_name

    def serialize(self):
        return (
            "{"
            + ", ".join([f'"{key}": "{value}"' for key, value in self.action_parameters.items()])
            + "}"
        )


class ActionsList(object):
    def __init__(self, *actions):
        assert all(
            isinstance(action, Action) for action in actions
        ), "actions must be list of Action objects!"

        self.action_parameters = actions

    def update_training_job_prefix(self, training_job_name):
        assert isinstance(training_job_name, str), "training_job_name must be a string!"

        for action in self.action_parameters:
            action.update_training_job_prefix(training_job_name)

    def serialize(self):
        return "[" + ", ".join([action.serialize() for action in self.action_parameters]) + "]"


class StopTraining(Action):
    def __init__(self, training_job_prefix=None):
        assert training_job_prefix is None or isinstance(
            training_job_prefix, str
        ), "training_job_name must be a string!"
        super().__init__(training_job_prefix=training_job_prefix)


class Email(Action):
    def __init__(self, email_address):
        assert isinstance(email_address, str), "email_address must be a string!"
        super().__init__(email_address=email_address)


class SMS(Action):
    def __init__(self, phone_number):
        assert isinstance(phone_number, str), "phone_number must be a string!"
        super().__init__(phone_number=phone_number)

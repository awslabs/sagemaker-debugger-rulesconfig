import json


def validate_action_str(action_str, action_parameters):
    """
    Parse the action string as JSON within an exec call. This mimics the same behavior in the rules container.

    If this triggers a syntax error, the exec call is set up incorrectly and needs to be fixed.
    If this triggers a JSON decode error, the action string is badly formatted.
    If this triggers an assertion error, the deserialized action JSON does not match the original action parameters.
    """
    try:
        exec(f'import json; assert json.loads("{action_str}") == {action_parameters}')
    except (SyntaxError, json.JSONDecodeError, AssertionError) as e:
        raise Exception(f"Error occurred during action string validation.")

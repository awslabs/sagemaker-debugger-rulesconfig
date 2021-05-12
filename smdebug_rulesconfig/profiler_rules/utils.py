invalid_boolean_error = "{0} accepts only boolean values for {1} "
invalid_key_format_error = "Key {0} does not follow naming scheme: <rule_name>_<parameter_name>"
invalid_rule_error = "{0} is an invalid rule name! Accepted case insensitive rule names are: {1}"
invalid_param_error = "{0} is an invalid parameter name! Accepted parameter names for {1} are: {2}"
invalid_positive_integer_error = "{0} {1} must be a positive integer!"
invalid_percentile_error = "{0} {1} must be a valid percentile!"


def validate_positive_integer(rule_name, key, val):
    assert val > 0, invalid_positive_integer_error.format(rule_name, key)


def validate_percentile(rule_name, key, val):
    assert 0 <= val <= 100, invalid_percentile_error.format(rule_name, key)


def validate_boolean(rule_name, key, val):
    assert isinstance(val, bool), invalid_boolean_error.format(rule_name, key)

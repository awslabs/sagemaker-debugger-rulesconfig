import pytest

from smdebug_rulesconfig.debugger_rules._constants import (
    SUPPORTED_DL_FRAMEWORKS,
    SUPPORTED_FRAMEWORKS,
)
from smdebug_rulesconfig.debugger_rules._ruleGroups import (
    DEEP_LEARNING_APPLICATION_RULES,
    DEEP_LEARNING_RULES,
    UNIVERSAL_RULES,
    XGBOOST_RULES,
)
from smdebug_rulesconfig.debugger_rules._utils import _get_rule_list


@pytest.mark.parametrize(
    "rule_list, framework_list",
    [
        (UNIVERSAL_RULES, SUPPORTED_FRAMEWORKS),
        (DEEP_LEARNING_RULES, SUPPORTED_DL_FRAMEWORKS),
        (DEEP_LEARNING_APPLICATION_RULES, SUPPORTED_DL_FRAMEWORKS),
        (XGBOOST_RULES, ["xgboost"]),
    ],
)
def test_framework_rule_compatibility(rule_list, framework_list):
    for rule in rule_list:
        for framework in framework_list:
            assert rule in _get_rule_list(framework), f"Rule: {rule} not supported by {framework}"

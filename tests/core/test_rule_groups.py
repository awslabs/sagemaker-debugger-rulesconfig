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


def test_universal_rules():
    for rule in UNIVERSAL_RULES:
        for framework in SUPPORTED_FRAMEWORKS:
            if rule not in _get_rule_list(framework):
                assert False, f"Rule: {rule} not supported by {framework}"


def test_deep_learning_rules():
    for rule in DEEP_LEARNING_RULES:
        for framework in SUPPORTED_DL_FRAMEWORKS:
            if rule not in _get_rule_list(framework):
                assert False, f"Rule: {rule} not supported by {framework}"


def test_deep_learning_application_rules():
    for rule in DEEP_LEARNING_APPLICATION_RULES:
        for framework in SUPPORTED_DL_FRAMEWORKS:
            if rule not in _get_rule_list(framework):
                assert False, f"Rule: {rule} not supported by {framework}"


def test_xgboost_rules():
    for rule in XGBOOST_RULES:
        if rule not in _get_rule_list("xgboost"):
            assert False, f"Rule: {rule} not supported by xgboost"

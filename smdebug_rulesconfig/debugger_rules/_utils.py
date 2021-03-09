import json
import os

from ._constants import (
    COLLECTION_CONFIG_FILE,
    RULE_CONFIG_FILE,
    SUPPORTED_DL_FRAMEWORKS,
    SUPPORTED_FRAMEWORKS,
)
from ._ruleGroups import (
    DEEP_LEARNING_RULES,
    DEEP_LEARNING_APPLICATION_RULES,
    UNIVERSAL_RULES,
    XGBOOST_RULES,
)


def _get_rule_config(rule_name):
    rule_config = None

    config_file_path = os.path.dirname(os.path.abspath(__file__)) + "/" + RULE_CONFIG_FILE

    if os.path.exists(config_file_path):
        with open(config_file_path) as json_data:
            configs = json.load(json_data)
            if rule_name in configs:
                rule_config = configs[rule_name]
    return rule_config


def _get_rule_list(framework):
    framework = framework.upper()
    assert framework in SUPPORTED_FRAMEWORKS

    rule_set = UNIVERSAL_RULES

    if framework in SUPPORTED_DL_FRAMEWORKS:
        rule_set = rule_set.union(DEEP_LEARNING_RULES).union(DEEP_LEARNING_APPLICATION_RULES)
    elif framework == "XGBOOST":
        rule_set = rule_set.union(XGBOOST_RULES)

    return list(rule_set)


def _get_config_for_group(rules):
    rules_config = []

    config_file_path = os.path.dirname(os.path.abspath(__file__)) + "/" + RULE_CONFIG_FILE

    if os.path.exists(config_file_path):
        with open(config_file_path) as json_data:
            configs = json.load(json_data)
            for rule_name in rules:
                if rule_name in configs:
                    rules_config.append(configs[rule_name])
    return rules_config


def _get_collection_config(collection_name):
    coll_config = None

    config_file_path = os.path.dirname(os.path.abspath(__file__)) + "/" + COLLECTION_CONFIG_FILE

    if os.path.exists(config_file_path):
        with open(config_file_path) as json_data:
            configs = json.load(json_data)
            if collection_name in configs:
                coll_config = configs[collection_name]
    return coll_config

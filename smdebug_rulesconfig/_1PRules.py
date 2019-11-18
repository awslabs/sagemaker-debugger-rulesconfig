import json
import os
from pathlib import Path

_rule_config_file = "rule_config_jsons/ruleConfigs.json"
_rule_groups_config_file = "rule_config_jsons/ruleGroups.json"

def _get_rule_config(rule_name):
    rule_config = None
    config_file_path = str(Path(__file__).parent.absolute()) + "/" + _rule_config_file

    if os.path.exists(config_file_path):
        with open(config_file_path) as json_data:
            configs = json.load(json_data)
            if rule_name in configs:
                rule_config = configs[rule_name]
    return rule_config

def _get_rule_list(framework, type):
    rules_list = []
    config_file_path = str(Path(__file__).parent.absolute()) + "/" + _rule_groups_config_file
    if os.path.exists(config_file_path):
        with open(config_file_path) as json_data:
            configs = json.load(json_data)
            if framework in configs:
                if type in configs[framework]:
                    rules_list = configs[framework][type]
    return rules_list

def _get_config_for_group(rules):
    rules_config = []
    config_file_path = str(Path(__file__).parent.absolute()) + "/" + _rule_config_file

    if os.path.exists(config_file_path):
        with open(config_file_path) as json_data:
            configs = json.load(json_data)
            for rule_name in rules:
                if rule_name in configs:
                    rules_config.append(configs[rule_name])
    return rules_config


def vanishing_gradient() :
    rule_config = _get_rule_config("VanishingGradient")
    return rule_config

def similar_across_runs() :
    rule_config = _get_rule_config("SimilarAcrossRuns")
    return rule_config

def weight_update_ratio() :
    rule_config = _get_rule_config("WeightUpdateRatio")
    return rule_config

def all_zero() :
    rule_config = _get_rule_config("AllZero")
    return rule_config

def exploding_tensor() :
    rule_config = _get_rule_config("ExplodingTensor")
    return rule_config

def unchanged_tensor() :
    rule_config = _get_rule_config("UnchangedTensor")
    return rule_config

def loss_not_decreasing() :
    rule_config = _get_rule_config("LossNotDecreasing")
    return rule_config

def check_input_images() :
    rule_config = _get_rule_config("CheckInputImages")
    return rule_config

def dead_relu() :
    rule_config = _get_rule_config("DeadRelu")
    return rule_config

def confusion() :
    rule_config = _get_rule_config("Confusion")
    return rule_config

def tree_depth() :
    rule_config = _get_rule_config("TreeDepth")
    return rule_config

def class_imbalance() :
    rule_config = _get_rule_config("ClassImbalance")
    return rule_config

def overfit() :
    rule_config = _get_rule_config("Overfit")
    return rule_config

def get_rule_groups(ruleEnum):
    ruleEnumVal = ruleEnum.value
    rules_config = _get_config_for_group(ruleEnumVal)
    return rules_config



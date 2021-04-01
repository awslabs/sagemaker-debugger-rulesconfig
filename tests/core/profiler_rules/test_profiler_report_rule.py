import pytest
import inspect

from smdebug_rulesconfig.profiler_rules.rules import CPUBottleneck, ProfilerReport
from smdebug_rulesconfig.profiler_rules.utils import (
    invalid_key_format_error,
    invalid_param_error,
    invalid_rule_error,
    invalid_percentile_error,
    invalid_positive_integer_error,
)


@pytest.fixture
def rule_names():
    return str([rule.__name__ for rule in ProfilerReport.get_rules()]).strip("[]")


def test_default_profiler_report_rule():
    rule = ProfilerReport()
    assert rule.rule_name == ProfilerReport.__name__
    assert rule.rule_parameters == {
        "rule_to_invoke": ProfilerReport.__name__,
        "custom_rule_parameters": {},
    }


def test_valid_profiler_report_rule_custom_params():
    rule = ProfilerReport(CPUBottleneck_threshold=30)
    assert rule.rule_name == ProfilerReport.__name__
    assert rule.rule_parameters == {
        "rule_to_invoke": ProfilerReport.__name__,
        "custom_rule_parameters": {"CPUBottleneck_threshold": 30},
    }

    # case of parameter doesn't matter
    rule = ProfilerReport(cpubottleneck_threshold=20)
    assert rule.rule_name == ProfilerReport.__name__
    assert rule.rule_parameters == {
        "rule_to_invoke": ProfilerReport.__name__,
        "custom_rule_parameters": {"CPUBottleneck_threshold": 20},
    }


def test_invalid_profiler_report_rule_custom_params(rule_names):
    # invalid parameter key format
    with pytest.raises(
        AssertionError, match=invalid_key_format_error.format("CPUBottleneckthreshold")
    ):
        ProfilerReport(CPUBottleneckthreshold=30)

    # invalid parameter key name (unknown rule)
    with pytest.raises(AssertionError, match=invalid_rule_error.format("BadRule", rule_names)):
        ProfilerReport(BadRule_threshold=30)

    # invalid parameter key name (unknown parameter)
    with pytest.raises(
        TypeError,
        match=invalid_param_error.format(
            "bad_param",
            CPUBottleneck.__name__,
            str(inspect.getfullargspec(CPUBottleneck.__init__)[0]).strip("[]"),
        ),
    ):
        ProfilerReport(CPUBottleneck_bad_param=30)

    # invalid parameter value (invalid percentile)
    with pytest.raises(
        AssertionError, match=invalid_percentile_error.format("CPUBottleneck", "threshold")
    ):
        ProfilerReport(CPUBottleneck_threshold=200)

    # invalid parameter value (invalid positive integer)
    with pytest.raises(
        AssertionError, match=invalid_positive_integer_error.format("CPUBottleneck", "patience")
    ):
        ProfilerReport(CPUBottleneck_patience=-1)

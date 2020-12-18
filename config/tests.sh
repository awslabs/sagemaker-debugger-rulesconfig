#!/usr/bin/env bash
# TODO: Add end to end sagemaker tests for each framework and version so that they can be run here.

set -eox pipefail


run_for_framework() {
    python -m pytest ${code_coverage_smdebug:+--cov=./ --cov-append}  --durations=50 --html=$REPORT_DIR/report_$1.html -v -s --self-contained-html tests/$1
}

export OUT_DIR=upload/$CURRENT_COMMIT_PATH
export REPORT_DIR=$OUT_DIR/pytest_reports

if [ "$run_pytest_core" = "enable" ] ; then
    run_for_framework core
fi

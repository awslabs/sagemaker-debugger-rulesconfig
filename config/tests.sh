#!/usr/bin/env bash
# TODO: Add end to end sagemaker tests for each framework and version so that they can be run here.

set -e
set -ex
set -o pipefail

export OUT_DIR=upload/$CURRENT_COMMIT_PATH
export REPORT_DIR=$OUT_DIR/pytest_reports
python -m pytest ${code_coverage_smdebug:+--cov=./ --cov-append}  --durations=50 --html=$REPORT_DIR/report_core.html -v -s --self-contained-html tests/core

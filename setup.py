# Standard Library
import os
import sys
import setuptools

exec(open("smdebug_rulesconfig/_version.py").read())
CURRENT_VERSION = __version__

def build_rule_config_package(version):
    setuptools.setup(
        name="smdebug_rulesconfig",
        version=version,
        author="AWS DeepLearning Team",
        description="SMDebug RulesConfig",
        url="https://github.com/awslabs/sagemaker-debugger-rulesconfig",
        packages=["smdebug_rulesconfig"],
        package_data={'smdebug_rulesconfig' : ['rule_config_jsons/*.json']},
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
        ],
        python_requires=">=2.7",
    )

build_rule_config_package(version=CURRENT_VERSION)


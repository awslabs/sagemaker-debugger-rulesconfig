# Standard Library
import setuptools

long_description = (
    "This library, intended to be used with [Amazon SageMaker Python SDK]("
    "https://github.com/aws/sagemaker-python-sdk), helps you specify builtin "
    "rules without worrying about any details or tweak the configuration of builtin rules. These "
    "builtin rules are available in Amazon SageMaker."
    "Amazon SageMaker Debugger Rulesconfig package can be used with Amazon SageMaker Debugger or as"
    "stand-alone rule config retriever. In addition to retrieving builtin rules, configuration for common collections can be retrieved as well."
)

exec(open("smdebug_rulesconfig/_version.py").read())
CURRENT_VERSION = __version__


def build_rule_config_package(version):
    setuptools.setup(
        name="smdebug_rulesconfig",
        version=version,
        author="AWS DeepLearning Team",
        description="SMDebug RulesConfig",
        long_description=long_description,
        url="https://github.com/awslabs/sagemaker-debugger-rulesconfig",
        packages=['smdebug_rulesconfig'],
        package_data={"smdebug_rulesconfig": ["debugger_rules/rule_config_jsons/*.json"]},
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
        ],
        python_requires=">=2.7",
        license="Apache License Version 2.0",
    )


build_rule_config_package(version=CURRENT_VERSION)

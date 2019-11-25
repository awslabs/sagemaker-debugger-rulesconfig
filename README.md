## SageMaker-Debugger-RulesConfig

Sagemaker-debugger is an upcoming AWS service designed to be a debugger for machine learning models. It lets you go beyond just looking at scalars like losses and accuracies during training and gives you full visibility into all tensors 'flowing through the graph' during training or inference.

SageMaker Debugger RulesConfig provides a mapping of builtin rules with default configurations. These configurations will affect both DebugHookConfig and DebugRuleConfigurations in the SageMaker Python SDK.

This library, intended to be used with SageMaker PySDK, helps you specify builtin rules without worrying about any details or tweak the configuration of builtin rules. These builtin rules are available in SageMaker.

SageMaker Debugger Rulesconfig package can be used with SageMaker Debugger or as stand-alone rule config retriever too. In addition to retrieving builtin rules, configuration for common collections can be retrieved as well.

Example: Vanilla builtin rule without customization

```
from sagemaker.debug import Rule
from smdebug_rulesconfig import vanishing_gradient

my_estimator = Estimator(
    ...
    rules=[Rule.sagemaker(vanishing_gradient())]
)
```

Example: Builtin rule with customization

```
my_estimator = Estimator(
    ...
    rules= [
        Rule.sagemaker(vanishing_gradient()),
        Rule.sagemaker(
            base_config=weight_update_ratio(),
            instance_type="t2.micro",
            name="my_wup_rule_name",
            container_local_path="/local/path",
            s3_output_path="s3://uri",
            volume_size_in_gb=100,
            rule_parameters={
                "param1": "value1",
                "param2": "value2"
            },
            collection_configurations=[
                CollectionConfiguration(
                    name="my_name",  # Required
                    parameters= {
                        "param1": "value1",
                        "param2": "value2"
                    }  # Required
                )
            ],
        )
    ],
    wait=False
)
```

Example: Builtin rule with collection configuration specified

```
from smdebug_rulesconfig import get_collection

my_estimator = Estimator(
    ...
    rules= [
        Rule.sagemaker(
            base_config=vanishing_gradient(),
            collection_configurations=[
                get_collection("weights")
            ],
        )
    ],
    wait=False
)
```

## License

This project is licensed under the Apache-2.0 License.


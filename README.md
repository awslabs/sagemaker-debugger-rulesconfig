## Amazon SageMaker Debugger RulesConfig

Amazon SageMaker Debugger is designed to be a debugger for machine learning models. It lets you go beyond just looking at scalars like losses and accuracies during training and gives you full visibility into all tensors 'flowing through the graph' during training or inference.

Amazon SageMaker Debugger RulesConfig provides a mapping of builtin rules with default configurations. These configurations will affect both DebugHookConfig and DebugRuleConfigurations in the Amazon SageMaker Python SDK.

This library, intended to be used with Amazon SageMaker Python SDK, helps you specify builtin rules without worrying about any details or tweak the configuration of builtin rules. These builtin rules are available in Amazon SageMaker.

Amazon SageMaker Debugger Rulesconfig package can be used with Amazon SageMaker Debugger or as stand-alone rule config retriever. In addition to retrieving builtin rules, configuration for common collections can be retrieved as well.

Example: Vanilla builtin rule without customization

```
from sagemaker.debugger import Rule, rule_configs

my_estimator = Estimator(
    ...
    rules=[Rule.sagemaker(rule_configs.vanishing_gradient())]
)
```

Example: Builtin rule with customization. For more details please refer to [Amazon SageMaker Python SDK](https://github.com/aws/sagemaker-python-sdk) documentation.

```
from sagemaker.debugger import Rule, CollectionConfig, rule_configs

my_estimator = Estimator(
    ...
    rules= [
        Rule.sagemaker(
            base_config=rule_configs.weight_update_ratio(),
            name="my_wup_rule_name",            # Optional
            container_local_path="/local/path", # Optional
            s3_output_path="s3://uri",          # Optional
            rule_parameters={
                "param1": "value1",
                "param2": "value2"
            }, # Optional
            collections_to_save=[
                CollectionConfig(
                    name="my_name",  # Required. If specified, debugger will collect tensors for this collection. Users may have to update rule_parameters above to run the rule on right tensors.
                    parameters= {
                        "param1": "value1",
                        "param2": "value2"
                    }  # Optional
                )
            ],
        )
    ]
)
```

## License

This project is licensed under the Apache-2.0 License.

# set of rules that are expected to work for all supported frameworks
# Supported Frameworks: Mxnet, Pytorch, Tensorflow, Xgboost
UNIVERSAL_RULES = {
    "AllZero",
    "ClassImbalance",
    "LossNotDecreasing",
    "Overfit",
    "Overtraining",
    "SimilarAcrossRuns",
    "StalledTrainingRule",
    "TensorVariance",
    "UnchangedTensor",
}

# set of rules that are expected to work for only for supported deep learning frameworks
# Supported Deep Learning Frameworks: Mxnet, Pytorch, Tensorflow
DEEP_LEARNING_RULES = {
    "DeadRelu",
    "ExplodingTensor",
    "PoorWeightInitialization",
    "SaturatedActivation",
    "VanishingGradient",
    "WeightUpdateRatio",
}

# Rules intended to be used as part of a DL Application
DEEP_LEARNING_APPLICATION_RULES = {"CheckInputImages", "NLPSequenceRatio"}

# Rules only compatible with XGBOOST
XGBOOST_RULES = {"Confusion", "FeatureImportanceOverweight", "TreeDepth"}

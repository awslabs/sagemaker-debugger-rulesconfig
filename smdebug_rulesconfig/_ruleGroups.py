from enum import Enum

class MXNET(Enum):
    SIMPLE = [
            "VanishingGradient",
            "LossNotDecreasing",
            "WeightUpdateRatio"
        ]
    ALL = []

class TENSORFLOW(Enum):
    SIMPLE = [
            "VanishingGradient",
            "LossNotDecreasing",
            "WeightUpdateRatio"
        ]
    ALL = []

class PYTORCH(Enum):
    SIMPLE = [
            "VanishingGradient",
            "LossNotDecreasing",
            "WeightUpdateRatio"
        ]
    ALL = []

class XGBOOST(Enum):
    SIMPLE = [
            "TreeDepth",
            "ClassImbalance"
        ]
    ALL = []
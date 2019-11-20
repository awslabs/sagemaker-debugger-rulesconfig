from ._utils import _get_collection_config


def weights():
    coll_config = _get_collection_config("weights")
    return coll_config


def gradients():
    coll_config = _get_collection_config("gradients")
    return coll_config


def losses():
    coll_config = _get_collection_config("losses")
    return coll_config


def input_image():
    coll_config = _get_collection_config("input_image")
    return coll_config


def relu_output():
    coll_config = _get_collection_config("relu_output")
    return coll_config


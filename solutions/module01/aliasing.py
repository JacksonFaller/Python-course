import copy


def independent_copy(value):
    return copy.copy(value)


def independent_deep_copy(value):
    return copy.deepcopy(value)

import copy


original = [1, 2, 3]
alias = original
alias.append(4)

print("original:", original)
print("alias:   ", alias)


def independent_copy(value):
    # TODO: return an independent shallow copy
    raise NotImplementedError


def independent_deep_copy(value):
    # TODO: return an independent deep copy
    raise NotImplementedError


if __name__ == "__main__":
    nested = [[1, 2], [3, 4]]
    shallow = independent_copy(nested)
    deep = independent_deep_copy(nested)
    shallow[0].append(99)
    print("nested:", nested)
    print("deep:  ", deep)

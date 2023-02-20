from typing import Any, Final


INPUT_LIST: Final[list[dict[str, int]]] = [
{'a': 1, 'b': 2, 'c': 3, 'd': 5},
{'c': 4, 'a': 3},
{'a': 1, 'd': 6},
{'a': 2, 'b': 2, 'd': 5},
{'e': 0}
]

#REFERENCE_DICT: Final[dict[str, int | list[int]]] = {'a': [1, 2, 3], 'b': 2, 'c': [3, 4], 'd': [5, 6], 'e': 0}

def association(INPUT_LIST):
    result = {}
    for _dict in INPUT_LIST:
        for key, value in _dict.items():

            if key in result:

                if type(result[key]) != list:
                    result.update({key: [result[key]]})

                result[key].append(value)
                result[key] = sorted(list(set(result[key])))

            else:
                result.update({key: value})
    return result

print(f"Задача 1:", association(INPUT_LIST))
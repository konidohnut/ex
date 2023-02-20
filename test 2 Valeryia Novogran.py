from typing import Any, Final

DICT = {'a': 1, 'b': 55, 'c': 39, 'd': -1, 'e': 0, 'f': 12}

def max_key(DICT):

    result_max_key = max(DICT, key=DICT.get)
    return result_max_key

def min_key(DICT):

    result_min_key = min(DICT, key=DICT.get)
    return result_min_key

print(f"Задача 2 max:", max_key (DICT))
print(f"Задача 2 min:", min_key (DICT))

import math
from typing import Tuple


def task_2_int(input_str: str) -> Tuple[int, int]:
    """Finds sum of integers in the input string and gets the maximum one"""
    sum_of_ints = 0
    max_int = -int(math.pow(10, 10))

    if len(input_str) == 0:
        return 0, 0

    input_str += "_"  # simplifies work with the last number
    current = ""
    for i in range(len(input_str)):
        if 47 < ord(input_str[i]) < 58:
            current += input_str[i]
        elif ord(input_str[i]) == 45 and current == "":
            current += "-"
        else:
            if len(current) > 0:
                current_number = int(current)
                sum_of_ints += current_number
                max_int = current_number if current_number > max_int else max_int
                current = ""

    return sum_of_ints, max_int


def task_2_float(input_str: str) -> Tuple[float, float]:
    """Finds sum of float values in the input string and the maximum one"""
    sum_of_floats = 0.0
    max_float = -math.pow(10, 10)

    if len(input_str) == 0:
        return 0, 0

    input_str += "_"  # simplifies work with the last number
    current = ""
    for i in range(len(input_str)):
        if 47 < ord(input_str[i]) < 58 or ord(input_str[i]) == 46:
            current += input_str[i]
        elif ord(input_str[i]) == 45 and current == "":
            current += "-"
        else:
            if len(current) > 0:
                current_number = float(current)
                sum_of_floats += current_number
                max_float = current_number if current_number > max_float else max_float
                current = ""

    return sum_of_floats, max_float


def task_2_word(input_str: str) -> str:
    """Finds the longest word"""
    result = ""

    current = ""
    for i in range(len(input_str)):
        if 64 < ord(input_str[i]) < 91 or 96 < ord(input_str[i]) < 123:
            current += input_str[i]
        else:
            if len(current) > 0:
                result = current if len(current) > len(result) else result
                current = ""

    return result

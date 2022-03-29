import math
from typing import Tuple


def task_2_int(input_str: str) -> Tuple[int, int]:
    """Finds sum of integers in the input string and gets the maximum one"""
    sum_of_ints = 0
    max_int = -int(math.pow(10, 10))

    if len(input_str) == 0:
        return 0, 0

    input_str += "_"  # simplifies work with the last number
    intermediate_result = ""
    for current_char in input_str:
        if 47 < ord(current_char) < 58:
            intermediate_result += current_char
        elif ord(current_char) == 45 and intermediate_result == "":
            intermediate_result += "-"
        else:
            if len(intermediate_result) > 0:
                current_number = int(intermediate_result)
                sum_of_ints += current_number
                max_int = current_number if current_number > max_int else max_int
                intermediate_result = ""

    return sum_of_ints, max_int


def task_2_float(input_str: str) -> Tuple[float, float]:
    """Finds sum of float values in the input string and the maximum one"""
    sum_of_floats = 0.0
    max_float = -math.pow(10, 10)

    if len(input_str) == 0:
        return 0, 0

    input_str += "_"  # simplifies work with the last number
    intermediate_result = ""
    for current_char in input_str:
        if 47 < ord(current_char) < 58 or ord(current_char) == 46:
            intermediate_result += current_char
        elif ord(current_char) == 45 and intermediate_result == "":
            intermediate_result += "-"
        else:
            if len(intermediate_result) > 0:
                current_number = float(intermediate_result)
                sum_of_floats += current_number
                max_float = current_number if current_number > max_float else max_float
                intermediate_result = ""

    return sum_of_floats, max_float


def task_2_word(input_str: str) -> str:
    """Finds the longest word"""
    result = ""

    intermediate_result = ""
    for current_char in input_str:
        if 64 < ord(current_char) < 91 or 96 < ord(current_char) < 123:
            intermediate_result += current_char
        else:
            if len(intermediate_result) > 0:
                result = intermediate_result if len(intermediate_result) > len(result) else result
                intermediate_result = ""

    return result

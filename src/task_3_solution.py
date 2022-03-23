from typing import List


def task_3_anagrams(input_list: List[str]) -> List[str]:
    """Finds anagrams and returns a list with anagrams only"""
    result = []

    if len(input_list) < 2:
        return result

    intermittent = {}
    for word in input_list:
        current_sorted = ''.join(sorted(word))
        if current_sorted not in intermittent.keys():
            intermittent[current_sorted] = word
        else:
            result.append(word)
            result.append(intermittent[current_sorted])

    return result


def task_3_anagrams_in_str(input_str: str) -> List[str]:
    return task_3_anagrams(input_list=input_str.split(" "))

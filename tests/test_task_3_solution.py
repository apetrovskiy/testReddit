import pytest
from typing import List

from src.task_3_solution import task_3_anagrams, task_3_anagrams_in_str

TEST_DATA_ANAGRAMS = [("original sample",
                       ['cat', 'act', 'dinosaur', 'testing',
                        'setting'], ['cat', 'act', 'testing', 'setting']),
                      ("one anagram", ["abc", "abc"], ["abc", "abc"]),
                      ("no anagrams", ["abc"], []), ("empty", [], [])]
TEST_DATA_ANAGRAMS_IN_STR = [
    ("original sample",
     "cat rocket tac testing dog setting carrot fix drone abc",
     ['cat', 'tac', 'testing', 'setting'])
]


@pytest.mark.parametrize("description,input_list,expected_list",
                         TEST_DATA_ANAGRAMS)
def test_task_3_anagrams(description: str, input_list: List[str],
                         expected_list: List[str]):
    actual_list = task_3_anagrams(input_list)

    assert sorted(actual_list) == sorted(
        expected_list
    ), f"The result list is wrong: expected = {expected_list}, actual = {actual_list}"


@pytest.mark.parametrize("description,input_str,expected_list",
                         TEST_DATA_ANAGRAMS_IN_STR)
def test_task_3_anagrams_in_str(description: str, input_str: str,
                                expected_list: List[str]):
    actual_list = task_3_anagrams_in_str(input_str)

    assert sorted(actual_list) == sorted(
        expected_list
    ), f"The result list is wrong: expected = {expected_list}, actual = {actual_list}"

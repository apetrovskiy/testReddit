import pytest

from src.task_2_solution import task_2_int, task_2_float, task_2_word

TEST_DATA_INT = [("333", 333, 333), ("222a#333", 333, 555), ("aaa333bbb444###555x", 555, 1332), ("", 0, 0),
                 ("-111", -111, -111), ("_#222aa333gh-444", 333, 111), ("111a111b111c111d11", 111, 455),
                 ("fRETre3445 43#$% 5п32424234 #$@$34 2323", 32424234, 32430084)]
TEST_DATA_FLOAT = [("333.0", 333.0, 333.0), ("222.0a#333", 333.0, 555.0), ("aaa333bbb444###555x", 555.0, 1332.0),
                   ("", 0.0, 0.0),
                   ("-111", -111.0, -111.0), ("_#222aa333gh-444.56", 333.0, 110.44)]

TEST_DATA_WORDS = [("aaaa#bbb3ccc", "aaaa"), ("", ""), ("abc,def", "abc"), ("#)&^", ""), ("2*3%4", "")]


@pytest.mark.parametrize("input_str,expected_max,expected_sum", TEST_DATA_INT)
def test_task_2_int(input_str: str, expected_max: int, expected_sum: int):
    actual_sum, actual_max = task_2_int(input_str)

    assert actual_max == expected_max, f"Maximum number is wrong, expected = {expected_max}, actual = {actual_max}"
    assert actual_sum == expected_sum, f"Sum is wrong, expected = {expected_sum}, actual = {actual_sum}"


@pytest.mark.parametrize("input_str,expected_max,expected_sum", TEST_DATA_FLOAT)
def test_task_2_float(input_str: str, expected_max: float, expected_sum: float):
    actual_sum, actual_max = task_2_float(input_str)

    assert actual_max == expected_max, f"Maximum number is wrong, expected = {expected_max}, actual = {actual_max}"
    assert actual_sum == expected_sum, f"Sum is wrong, expected = {expected_sum}, actual = {actual_sum}"


@pytest.mark.parametrize("input_str,expected_word", TEST_DATA_WORDS)
def test_task_2_word(input_str: str, expected_word: str):
    actual_word = task_2_word(input_str)

    assert actual_word == expected_word, f"The longest word is wrong, expected = {expected_word}, actual = {actual_word}"

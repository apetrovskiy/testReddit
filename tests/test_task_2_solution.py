import pytest

from src.task_2_solution import task_2_int, task_2_float, task_2_word

TEST_DATA_INT = [
    ("one number", "333", 333, 333),
    ("two numbers", "222a#333", 333, 555),
    ("three numbers", "aaa333bbb444###555x", 555, 1332),
    ("empty", "", 0, 0),
    ("negative", "-111", -111, -111),
    ("positive and negative", "_#222aa333gh-444", 333, 111),
    ("similar numbers", "111a111b111c111d11", 111, 455),
    ("original sample", "fRETre3445 43#$% 5п32424234 #$@$34 2323", 32424234, 32430084),
]
TEST_DATA_FLOAT = [
    ("one number", "333.0", 333.0, 333.0),
    ("two numbers", "222.0a#333", 333.0, 555.0),
    ("three numbers", "aaa333bbb444###555x", 555.0, 1332.0),
    ("empty", "", 0.0, 0.0),
    ("negative", "-111", -111.0, -111.0),
    ("positive and negative", "_#222aa333gh-444.56", 333.0, 110.44),
    ("original sample", "fRETre3445 43#$% 5п32424234 #$@$34 2323", 32424234, 32430084),
]

TEST_DATA_WORDS = [
    ("a clear case", "aaaa#bbb3ccc", "aaaa"),
    ("empty", "", ""),
    ("equal-length words", "abc,def", "abc"),
    ("original sample", "#)&^", ""),
    ("no words at all", "2*3%4", ""),
]


@pytest.mark.parametrize(
    "description,input_str,expected_max,expected_sum", TEST_DATA_INT
)
def test_task_2_int(
    description: str, input_str: str, expected_max: int, expected_sum: int
):
    actual_sum, actual_max = task_2_int(input_str)

    assert (
        actual_max == expected_max
    ), f"Maximum number is wrong, expected = {expected_max}, actual = {actual_max}"
    assert (
        actual_sum == expected_sum
    ), f"Sum is wrong, expected = {expected_sum}, actual = {actual_sum}"


@pytest.mark.parametrize(
    "description,input_str,expected_max,expected_sum", TEST_DATA_FLOAT
)
def test_task_2_float(
    description: str, input_str: str, expected_max: float, expected_sum: float
):
    actual_sum, actual_max = task_2_float(input_str)

    assert (
        actual_max == expected_max
    ), f"Maximum number is wrong, expected = {expected_max}, actual = {actual_max}"
    assert (
        actual_sum == expected_sum
    ), f"Sum is wrong, expected = {expected_sum}, actual = {actual_sum}"


@pytest.mark.parametrize("description,input_str,expected_word", TEST_DATA_WORDS)
def test_task_2_word(description: str, input_str: str, expected_word: str):
    actual_word = task_2_word(input_str)

    assert (
        actual_word == expected_word
    ), f"The longest word is wrong, expected = {expected_word}, actual = {actual_word}"

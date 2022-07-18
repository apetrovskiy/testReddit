from typing import List, Dict

import pytest

from src.task_4_solution import task_4_solution

TEST_DATA = [
    (
        "",
        {"Alex": 56, "Kate": 78, "Maria": 43, "Dmitry": 65},
        {"Dmitry": 47, "Wei": 99, "Maria": 43},
        ["Wei"],
        ["Alex", "Kate"],
        "Dmitry",
        112,
    )
]


@pytest.mark.parametrize(
    "description,math_students,info_students,math_missing,info_missing,expected_best_student,expected_best_score",
    TEST_DATA,
)
def test_task_2_int(
    description: str,
    math_students: Dict,
    info_students: Dict,
    math_missing: List,
    info_missing: List,
    expected_best_student,
    expected_best_score,
):
    (
        actual_math_missing,
        actual_info_missing,
        actual_top_student,
        actual_top_score,
    ) = task_4_solution(math_students, info_students)

    assert actual_math_missing == math_missing, f"Maximum number is wrong, expected = "
    assert actual_info_missing == info_missing, f"Sum is wrong, expected = "
    assert actual_top_student == expected_best_student, ""
    assert actual_top_score == expected_best_score, ""

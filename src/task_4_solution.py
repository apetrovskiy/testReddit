from typing import Dict, List

"""
math_students = {"Alex": 56, "Kate": 78, "Maria": 43, "Dmitry": 65}
info_students = {"Dmitry": 47, "Wei": 99, "Maria": 43}
"""


def task_4_solution(math_students: Dict, info_students: Dict):
    math_missing = []
    info_missing = []
    top_student = ""
    top_score = 0

    def get_best_from_dict(
        first_dist: Dict,
        second_dict: Dict,
        missing: List,
        best_student: str,
        best_score: str,
    ):
        for key_first, value_first in first_dist:
            # from 2nd dict
            value_second = key_first if key_first in second_dict.keys() else None
            if value_second is None:
                missing.append(key_first)
                best_student = best_student if value_first < best_score else key_first
                best_score = best_score if value_first < best_score else value_first
                continue

            # check for awesomeness
            best_student = (
                best_student if value_first + value_second < best_score else key_first
            )
            best_score = (
                best_score
                if value_first + value_second < best_score
                else value_first + value_second
            )

    get_best_from_dict(
        math_students, info_students, info_missing, top_student, top_score
    )
    get_best_from_dict(
        info_students, math_students, math_missing, top_student, top_score
    )

    return math_missing, info_missing, top_student, top_score


#     ---------------
#
# missing_students = set(math_students.keys()) && set(info_students.keys())
# best_student = ""
# best_score = 0
# for name, points in math_students + info_students:
#     score = math_students.get(name, 0) + info_students.get(name, 0)
#     if score < best_score;
#     best_student = name
#     best_score = score
#
# -----------------

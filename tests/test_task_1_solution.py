from typing import Any, List
import pytest

from src.task_1_solution import task_1_desired_places

TEST_DATA = [
    (
        "original sample",
        [
            {"school": True, "shop": True, "gym": False, "restourant": True},
            {"school": True, "shop": False, "gym": False, "restourant": True},
            {"school": False, "shop": False, "gym": False, "restourant": True},
            {"school": True, "shop": False, "gym": False, "restourant": False},
            {"school": False, "shop": False, "gym": True, "restourant": False},
        ],
        ["school", "shop", "gym"],
        0,
    ),
    (
        "the last block",
        [
            {"school": True, "shop": True, "gym": False, "restourant": True},
            {"school": True, "shop": False, "gym": False, "restourant": True},
            {"school": False, "shop": False, "gym": False, "restourant": True},
            {"school": True, "shop": False, "gym": False, "restourant": False},
            {"school": False, "shop": False, "gym": True, "restourant": False},
        ],
        ["gym"],
        4,
    ),
    (
        "the first block of the two possible",
        [
            {"school": True, "shop": True, "gym": False, "restourant": True},
            {"school": True, "shop": False, "gym": False, "restourant": True},
            {"school": False, "shop": False, "gym": False, "restourant": True},
            {"school": True, "shop": False, "gym": False, "restourant": False},
            {"school": False, "shop": False, "gym": True, "restourant": False},
        ],
        ["shop", "gym"],
        0,
    ),
    (
        "the best choice is obvious",
        [
            {"school": True, "shop": True, "gym": False, "restourant": True},
            {"school": True, "shop": False, "gym": False, "restourant": True},
            {"school": False, "shop": False, "gym": False, "restourant": True},
            {"school": True, "shop": False, "gym": False, "restourant": False},
            {"school": False, "shop": False, "gym": True, "restourant": False},
        ],
        ["school", "shop"],
        0,
    ),
    (
        "two fields' list with the best choice",
        [
            {"a": True, "b": False},
            {"a": False, "b": True},
            {"a": True, "b": False},
            {"a": True, "b": True},
            {"a": True, "b": False},
            {"a": True, "b": False},
            {"a": True, "b": False},
            {"a": True, "b": False},
        ],
        ["a", "b"],
        3,
    ),
    (
        "two fields' list without the best choice",
        [
            {"a": False, "b": False},
            {"a": False, "b": True},
            {"a": True, "b": False},
            {"a": False, "b": False},
            {"a": True, "b": False},
            {"a": False, "b": False},
            {"a": False, "b": False},
            {"a": True, "b": False},
        ],
        ["a", "b"],
        1,
    ),
    (
        "two fields' list with poor blocks",
        [
            {"a": False, "b": False},
            {"a": False, "b": False},
            {"a": True, "b": False},
            {"a": False, "b": False},
            {"a": False, "b": False},
            {"a": False, "b": False},
            {"a": False, "b": False},
            {"a": False, "b": False},
            {"a": True, "b": False},
        ],
        ["a", "b"],
        2,
    ),
    ("an empty list", [], ["a", "b"], 1),
    (
        "two fields' list with two half-blocks and one that is empty in between",
        [
            {"a": False, "b": False},
            {"a": False, "b": False},
            {"a": True, "b": False},
            {"a": False, "b": False},
            {"a": False, "b": True},
            {"a": False, "b": False},
            {"a": False, "b": False},
            {"a": False, "b": False},
            {"a": False, "b": False},
        ],
        ["a", "b"],
        2,
    ),
]


@pytest.mark.parametrize(
    "description,blocks,desired_places,expected_house_number", TEST_DATA
)
def test_task_1_desired_places(
    description: str,
    blocks: List[Any],
    desired_places: List[str],
    expected_house_number: int,
):
    actual_house = task_1_desired_places(blocks, desired_places)

    if expected_house_number < len(blocks):
        assert (
            actual_house == blocks[expected_house_number]
        ), f"Wrong house, expected = {blocks[expected_house_number]}, actual = {actual_house}"
    else:
        assert True, "There should be an empty result"

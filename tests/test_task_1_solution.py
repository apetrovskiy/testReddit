from typing import Any, List
import pytest

from src.task_1_solution import task_1_desired_places, task_1_desired_places_new, task_1_desired_places_new_2nd

TEST_DATA = [("original sample", [{
    'school': True,
    'shop': True,
    'gym': False,
    'restourant': True
}, {
    'school': True,
    'shop': False,
    'gym': False,
    'restourant': True
}, {
    'school': False,
    'shop': False,
    'gym': False,
    'restourant': True
}, {
    'school': True,
    'shop': False,
    'gym': False,
    'restourant': False
}, {
    'school': False,
    'shop': False,
    'gym': True,
    'restourant': False
}], ['school', 'shop', 'gym'], 0),
             ("the last block", [{
                 'school': True,
                 'shop': True,
                 'gym': False,
                 'restourant': True
             }, {
                 'school': True,
                 'shop': False,
                 'gym': False,
                 'restourant': True
             }, {
                 'school': False,
                 'shop': False,
                 'gym': False,
                 'restourant': True
             }, {
                 'school': True,
                 'shop': False,
                 'gym': False,
                 'restourant': False
             }, {
                 'school': False,
                 'shop': False,
                 'gym': True,
                 'restourant': False
             }], ['gym'], 4),
             ("the first block of the two possible", [{
                 'school': True,
                 'shop': True,
                 'gym': False,
                 'restourant': True
             }, {
                 'school': True,
                 'shop': False,
                 'gym': False,
                 'restourant': True
             }, {
                 'school': False,
                 'shop': False,
                 'gym': False,
                 'restourant': True
             }, {
                 'school': True,
                 'shop': False,
                 'gym': False,
                 'restourant': False
             }, {
                 'school': False,
                 'shop': False,
                 'gym': True,
                 'restourant': False
             }], ['shop', 'gym'], 0),
             ("the best choice is obvious", [{
                 'school': True,
                 'shop': True,
                 'gym': False,
                 'restourant': True
             }, {
                 'school': True,
                 'shop': False,
                 'gym': False,
                 'restourant': True
             }, {
                 'school': False,
                 'shop': False,
                 'gym': False,
                 'restourant': True
             }, {
                 'school': True,
                 'shop': False,
                 'gym': False,
                 'restourant': False
             }, {
                 'school': False,
                 'shop': False,
                 'gym': True,
                 'restourant': False
             }], ['school', 'shop'], 0)]


@pytest.mark.parametrize(
    "description,blocks,desired_places,expected_house_number", TEST_DATA)
def test_task_1_desired_places_new_2nd(description: str, blocks: List[Any],
                                       desired_places: List[str],
                                       expected_house_number: int):
    actual_house = task_1_desired_places_new_2nd(blocks, desired_places)

    assert actual_house == blocks[
        expected_house_number], f"Wrong house, expected = {blocks[expected_house_number]}, actual = {actual_house}"

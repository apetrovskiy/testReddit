from typing import Any, List
import pytest

from src.task_1_solution import task_1_desired_places, task_1_desired_places_new

TEST_DATA = [([
                  {
                      'school': True,
                      'shop': True,
                      'gym': False,
                      'restourant': True
                  },
                  {
                      'school': True,
                      'shop': False,
                      'gym': False,
                      'restourant': True
                  },
                  {
                      'school': False,
                      'shop': False,
                      'gym': False,
                      'restourant': True
                  },
                  {
                      'school': True,
                      'shop': False,
                      'gym': False,
                      'restourant': False
                  },
                  {
                      'school': False,
                      'shop': False,
                      'gym': True,
                      'restourant': False
                  }
              ], ['school', 'shop', 'gym'], 0),
    ([
         {
             'school': True,
             'shop': True,
             'gym': False,
             'restourant': True
         },
         {
             'school': True,
             'shop': False,
             'gym': False,
             'restourant': True
         },
         {
             'school': False,
             'shop': False,
             'gym': False,
             'restourant': True
         },
         {
             'school': True,
             'shop': False,
             'gym': False,
             'restourant': False
         },
         {
             'school': False,
             'shop': False,
             'gym': True,
             'restourant': False
         }
     ], ['gym'], 4),
    ([
         {
             'school': True,
             'shop': True,
             'gym': False,
             'restourant': True
         },
         {
             'school': True,
             'shop': False,
             'gym': False,
             'restourant': True
         },
         {
             'school': False,
             'shop': False,
             'gym': False,
             'restourant': True
         },
         {
             'school': True,
             'shop': False,
             'gym': False,
             'restourant': False
         },
         {
             'school': False,
             'shop': False,
             'gym': True,
             'restourant': False
         }
     ], ['shop', 'gym'], 0), ([
                                  {
                                      'school': True,
                                      'shop': True,
                                      'gym': False,
                                      'restourant': True
                                  },
                                  {
                                      'school': True,
                                      'shop': False,
                                      'gym': False,
                                      'restourant': True
                                  },
                                  {
                                      'school': False,
                                      'shop': False,
                                      'gym': False,
                                      'restourant': True
                                  },
                                  {
                                      'school': True,
                                      'shop': False,
                                      'gym': False,
                                      'restourant': False
                                  },
                                  {
                                      'school': False,
                                      'shop': False,
                                      'gym': True,
                                      'restourant': False
                                  }
                              ], ['school', 'shop'], 0)
]


@pytest.mark.parametrize("blocks,desired_places,expected_house_number", TEST_DATA)
def test_task_1_desired_places_new(blocks: List[Any], desired_places: List[str], expected_house_number: int):
    actual_house = task_1_desired_places_new(blocks, desired_places)

    assert actual_house == blocks[
        expected_house_number], f"Wrong house, expected = {blocks[expected_house_number]}, actual = {actual_house}"

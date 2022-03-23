import json
from typing import Any, List


def task_1_desired_places(blocks: List[Any]) -> int:
    """Returns a house with optimum conditions"""
    desired_house_number = -1

    # house fields
    HOUSE_ID = 'id'
    SCHOOL = 'school'
    SHOP = 'shop'
    GYM = 'gym'
    RESTAURANT = 'restourant'

    house_scores = []
    last_school = last_shop = last_gym = last_restaurant = -1_000_000_000

    for i in range(len(blocks)):
        house = blocks[i]
        print(house)
        house_score = {HOUSE_ID: i}
        house_score[SCHOOL] = 0 if house[SCHOOL] else i - last_school
        last_school = i if house[SCHOOL] else last_school
        house_score[SHOP] = 0 if house[SHOP] else i - last_shop
        last_shop = i if house[SHOP] else last_shop
        house_score[GYM] = 0 if house[GYM] else i - last_gym
        last_gym = i if house[GYM] else last_gym
        house_score[RESTAURANT] = 0 if house[RESTAURANT] else i - last_restaurant
        last_restaurant = i if house[RESTAURANT] else last_restaurant

        house_scores.append(house_score)

    print(house_scores)

    # getting the best choice - with minimum scores
    # for i in range(len(house_scores)):


    return blocks[desired_house_number]

import json
from typing import Any, List


def task_1_desired_places(blocks: List[Any], desired_places: List[str]) -> int:
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
        house_score[
            RESTAURANT] = 0 if house[RESTAURANT] else i - last_restaurant
        last_restaurant = i if house[RESTAURANT] else last_restaurant

        house_scores.append(house_score)

    print(house_scores)

    # getting the best choice - with minimum scores
    efficiency_of_houses = {}
    for house_score in house_scores:
        efficiency_of_house = {'id': house_score['id']}
        print(efficiency_of_house)
        efficiency = 0
        for place in desired_places:
            efficiency += house_score[place]
            # efficiency_of_house = {id:house_score.id, efficiency = }
        efficiency_of_house['score'] = efficiency
        print(efficiency_of_house)
        efficiency_of_houses[
            efficiency_of_house['id']] = efficiency_of_house['score']
    # best_choice = {(key, val) for key, val in efficiency_of_houses}
    best_choice = min(efficiency_of_houses, key=efficiency_of_houses.get)

    print(efficiency_of_houses)
    print(best_choice)

    # return blocks[desired_house_number]
    return blocks[best_choice]


def task_1_desired_places_new(blocks: List[Any],
                              desired_places: List[str]) -> int:
    """Returns a house with optimum conditions"""
    best_choice = -1

    block_scores = {}
    for i in range(len(blocks)):
        current_block = blocks[i]
        block_score = {'id': i}
        overall_block_score = 0
        for place in desired_places:
            if current_block[place]:
                overall_block_score += 2
            if not blocks[i][place] and i > 0:
                print(block_score['id'])
                print(block_score['id'] - 1)
                print(block_scores[block_score['id'] - 1])
                block_scores[block_score['id'] - 1]['score'] += 1
        block_score['score'] = overall_block_score
        block_scores[block_score['id']] = block_score['score']

    best_choice = min(block_scores, key=block_scores.get)

    return blocks[best_choice]


def task_1_desired_places_new_2nd(blocks: List[Any],
                                  desired_places: List[str]) -> int:
    """Returns a house with optimum conditions"""
    best_choice = -1

    block_scores = {}
    for i in range(len(blocks)):
        current_block = blocks[i]
        block_score = {'id': i}
        overall_block_score = 0
        for place in desired_places:
            if current_block[place]:
                overall_block_score += 1
        block_score['score'] = overall_block_score
        block_scores[block_score['id']] = block_score['score']

    print(block_scores)
    best_choice = max(block_scores, key=block_scores.get)
    print(best_choice)

    return blocks[best_choice]
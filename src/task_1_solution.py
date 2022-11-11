from typing import Any, List


def task_1_desired_places(blocks: List[Any], desired_places: List[str]) -> int:
    """Returns a block with optimum conditions"""
    best_choice = -1

    if len(blocks) == 0:
        return {}

    block_scores = {}
    for i in range(len(blocks)):
        current_block = blocks[i]
        block_score = {"id": i}
        overall_block_score = 0
        for place in desired_places:
            if current_block[place]:
                overall_block_score += 1
        block_score["score"] = overall_block_score
        block_scores[block_score["id"]] = block_score["score"]

    best_choice = max(block_scores, key=block_scores.get)

    return blocks[best_choice]

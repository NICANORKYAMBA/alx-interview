#!/usr/bin/python3
"""Function that checks if all boxes can be opened"""


def canUnlockAll(boxes):
    """Function that checks if all boxes can be opened
    Args:
        boxes: list of lists of integers

    Returns:
        True if all boxes can be opened and False otherwise
    """
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key >= 0 and key < num_boxes and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)

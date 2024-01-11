#!/usr/bin/python3
""" module for lockboxes
"""


def canUnlockAll(boxes):
    """ Set to keep track of opened boxes """

    opened_boxes = {0}
    queue = [0]
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                queue.append(key)

    return len(opened_boxes) == len(boxes)

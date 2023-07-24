#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon July  24 13:00:00 2023

@Author: Nicanor Kyamba
"""


def validUTF8(data):
    """
    Determines if a given data set is valid UTF-8.

    Args:
        data (list): A list of integers.

    Returns:
        bool: True if the data set is valid UTF-8, False otherwise.
    """
    num_of_bytes = 0

    for byte in data:
        if num_of_bytes == 0:
            if byte < 128:
                continue

            if 192 <= byte < 224:
                num_of_bytes = 1
            elif 224 <= byte < 240:
                num_of_bytes = 2
            elif 240 <= byte < 248:
                num_of_bytes = 3
            else:
                return False
        else:
            if 128 <= byte < 192:
                num_of_bytes -= 1
            else:
                return False
    return True

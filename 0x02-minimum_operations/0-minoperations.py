#!/usr/bin/python3
"""Min operations"""


def minOperations(n):
    """
    Function that returns the minimum number of operations

    Args:
        n (int): number of elements

    Returns:
        int: minimum number of operations
    """
    if n <= 1:
        return 0

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)

    return n

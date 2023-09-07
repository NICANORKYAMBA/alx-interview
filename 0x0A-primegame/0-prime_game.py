#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thur Sep  7 10:00:00 2023

@Author: Nicanor Kyamba
"""


def isWinner(x, nums):
    """
    Function that checks for the winner of the game

    Args:
        x (int): The number of rounds
        nums (list): The list of rounds

    Returns:
        str: The winner
    """
    if not nums or x < 1:
        return None
    max_num = max(nums)

    # Create a filter to mark prime numbers
    my_filter = [True for _ in range(max(max_num + 1, 2))]

    # Use the Sieve of Eratosthenes to mark non-prime numbers
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not my_filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            my_filter[j] = False

    # Mark 0 and 1 as non-prime
    my_filter[0] = my_filter[1] = False

    # Count the cumulative prime numbers
    y = 0
    for i in range(len(my_filter)):
        if my_filter[i]:
            y += 1
        my_filter[i] = y

    # Calculate the number of rounds won by Player 1 (Maria)
    player1 = 0
    for round_num in nums:
        player1 += my_filter[round_num] % 2 == 1

    # Determine the winner
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"

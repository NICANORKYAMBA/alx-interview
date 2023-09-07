#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thur Sep  7 10:00:00 2023

@Author: Nicanor Kyamba
"""


def is_prime(n):
    """
    Function to check if a number is prime

    Args:
        n (int): number to check

    Returns:
        bool: True if prime, False if not
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    """
    Function to check if Maria or Ben wins the game

    Args:
        x (int): number of rounds
        nums (list): list of numbers

    Returns:
        str: "Maria" or "Ben" or None
    """
    if x <= 0 or not nums:
        return None

    ben_wins = 0
    maria_wins = 0

    for n in nums:
        prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))

        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

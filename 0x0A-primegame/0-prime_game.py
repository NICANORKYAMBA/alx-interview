#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thur Sep  7 10:00:00 2023

@Author: Nicanor Kyamba
"""


def isWinner(x, nums):
    """
    Find the winner of the game.

    Args:
        x (int): The number of rounds
        nums (list): The list of numbers

    Returns:
        str: The winner
    """
    def sieve_eratosthenes(limit):
        """
        Sieve of Eratosthenes.

        Args:
            limit (int): The limit of the sieve

        Returns:
            list: The list of primes
        """
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        primes = []

        for current in range(2, limit + 1):
            if sieve[current]:
                primes.append(current)
                for multiple in range(current * current, limit + 1, current):
                    sieve[multiple] = False

        return primes

    def can_win(round_num, primes):
        """
        Check if Maria can win.

        Args:
            round_num (int): The round number
            primes (list): The list of primes

        Returns:
            bool: True if Maria can win, False otherwise
        """
        if round_num % 2 == 0:
            return False
        for prime in primes:
            if round_num % prime == 0:
                return True
        return False

    if max(nums) <= 1:
        return None

    primes = sieve_eratosthenes(max(nums))
    maria_wins = sum(1 for round_num in nums if can_win(round_num, primes))
    ben_wins = len(nums) - maria_wins

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

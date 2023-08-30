#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  30 15:00:00 2023

@Author: Nicanor Kyamba

Island Perimeter
"""


def island_perimeter(grid):
    """
    Find the perimeter of the island described in grid

    Args:
        grid: 2D array of 0s and 1s

    Returns:
        perimeter: the perimeter of the island
    """
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                # Check left
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Check right
                if col == len(grid[0]) - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
                # Check up
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Check down
                if row == len(grid) - 1 or grid[row + 1][col] == 0:
                    perimeter += 1

    return perimeter

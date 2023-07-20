#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thur July 20 15:00:00 2023

@Author: Nicanor Kyamba
"""
import sys

STATUSES = {'200': 0, '301': 0, '400': 0,
            '401': 0, '403': 0, '404': 0,
            '405': 0, '500': 0}


def print_stats(file_size, status_counts):
    """
    Prints the status code and the number of requests for
    that code

    Parameters
    ----------
    file_size : int
        The size of the file in bytes
    status_counts : dict
        A dictionary where the keys are the status codes
        and the values are the number of requests for
        that code

    Returns
    -------
    None
    """
    print('File size: {:d}'.format(file_size))
    for status in sorted(status_counts.keys()):
        if status_counts[status] != 0:
            print('{}: {:d}'.format(status, status_counts[status]))


def process_line(line, file_size, status_counts):
    line_parts = line.split()
    if len(line_parts) != 9:
        return

    status_code = line_parts[-2]
    try:
        file_size += int(line_parts[-1])
        status_counts[status_code] += 1
    except ValueError:
        pass

    return file_size, status_counts


if __name__ == '__main__':
    file_size = 0
    status_counts = STATUSES.copy()
    line_count = 0

    try:
        for line in sys.stdin:
            file_size, status_counts = process_line(
                    line.strip(), file_size, status_counts)
            line_count += 1

            if line_count % 10 == 0:
                print_stats(file_size, status_counts)

        print_stats(file_size, status_counts)

    except KeyboardInterrupt:
        print_stats(file_size, status_counts)

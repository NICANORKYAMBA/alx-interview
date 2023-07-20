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
    Print the number of status code and the file size

    Args:
        file_size (int): file size
        status_counts (dict): status counts

    Returns:
        None
    """
    print('File size: {:d}'.format(file_size))
    for status in sorted(status_counts.keys()):
        if status_counts[status] != 0:
            print('{}: {:d}'.format(status, status_counts[status]))


if __name__ == '__main__':
    file_size = 0
    line_count = 0
    status_counts = STATUSES.copy()

    try:
        for line in sys.stdin:
            line_parts = line.split()
            if len(line_parts) != 9:
                continue

            status_code = line_parts[-2]
            try:
                file_size += int(line_parts[-1])
                status_counts[status_code] += 1
            except ValueError:
                pass

            line_count += 1
            if line_count % 10 == 0:
                print_stats(file_size, status_counts)

    except KeyboardInterrupt:
        print_stats(file_size, status_counts)
        raise

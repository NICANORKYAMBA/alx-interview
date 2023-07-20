#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thur July 20 15:00:00 2023

@Author: Nicanor Kyamba
"""
import sys


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


if __name__ == '__main__':
    status_counts = {'200': 0, '301': 0, '400': 0,
                     '401': 0, '403': 0, '404': 0,
                     '405': 0, '500': 0}
    line_count = 0
    file_size = 0

    try:
        for line in sys.stdin:
            if line_count != 0 and line_count % 10 == 0:
                print_stats(file_size, status_counts)

            status_list = line.split()
            line_count += 1

            try:
                file_size += int(status_list[-1])
            except Exception:
                pass

            try:
                if status_list[-2] in status_counts:
                    status_counts[status_list[-2]] += 1
            except Exception:
                pass
            print_stats(file_size, status_counts)

    except KeyboardInterrupt:
        print_stats(file_size, status_counts)
        raise

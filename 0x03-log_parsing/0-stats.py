#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thur July 20 15:00:00 2023

@Author: Nicanor Kyamba
"""
import sys

STATUSES = ['200', '301', '400', '401', '403', '404', '405', '500']


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
    print(f'File size: {file_size}')
    for status in sorted(status_counts):
        count = status_counts[status]
        print(f'{status}: {count}')


def parse_line(line):
    """
    Parses a line from the file

    Parameters
    ----------
    line : str
        A line from the file

    Returns
    -------
    int
        The size of the file in bytes
    """
    parts = line.split()
    if len(parts) != 9:
        return None, None
    ip, _, _, status, size = parts[:5]
    if not status.isdigit() or status not in STATUSES:
        return None, None
    return ip, int(size)


def main():
    """
    Main function
    """
    file_size = 0
    status_counts = {status: 0 for status in STATUSES}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            ip, size = parse_line(line)
            if ip is None:
                continue

            file_size += size
            status_counts[status] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(file_size, status_counts)

    except KeyboardInterrupt:
        print_stats(file_size, status_counts)


if __name__ == '__main__':
    main()

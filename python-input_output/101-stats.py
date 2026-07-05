#!/usr/bin/python3
"""Module for computing input/output statistics from stdin."""

import sys


def print_info():
    """Print the current file size and status code statistics."""
    print('File size: {:d}'.format(file_size))

    for scode, code_times in sorted(status_codes.items()):
        if code_times > 0:
            print('{}: {:d}'.format(scode, code_times))


status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

lc = 0
file_size = 0


def main():
    """Read stdin lines and print status code statistics."""
    global lc, file_size, status_codes

    lc = 0
    file_size = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }

    try:
        for line in sys.stdin:
            if lc != 0 and lc % 10 == 0:
                print_info()

            pieces = line.split()

            try:
                status = int(pieces[-2])

                if str(status) in status_codes.keys():
                    status_codes[str(status)] += 1
            except Exception:
                pass

            try:
                file_size += int(pieces[-1])
            except Exception:
                pass

            lc += 1

        print_info()
    except KeyboardInterrupt:
        print_info()
        raise


if __name__ == "__main__":
    main()

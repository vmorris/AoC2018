
from collections import Counter
from itertools import chain
import time


def get_input_lines(file_to_read):
    with open(file_to_read, 'r') as f:
        return f.readlines()


def run_timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        run_time = end_time - start_time
        print(f'runtime: {run_time}')
    return wrapper


def check_frequency(line, occurrences):
    """
    Determine if any letter occurs in a string some specific number of times.
    :param line: string to check
    :param occurrences: number of times the letter must appear
    :return: boolean
    """
    counts = (Counter(line))
    if len([k for k,v in counts.items() if v == occurrences]) >= 1:
        return True
    else:
        return False


def match_strings(s1, s2, not_matching):
    """
    Compares characters in two strings, allowing for some to not match
    :param s1: first string
    :param s2: second string
    :param not_matching: specific number of characters that should not match
    :return: boolean
    """
    count = sum(s1[i] != s2[i] for i in range(len(s1)))
    return count == not_matching


def flatten_and_count_char(matrix, to_count):
    """
    Flattens an n-dimensional list and then counts the number of occurrences of a specific string.
    :param matrix: n-dimensional list
    :param to_count: string to count
    :return:
    """
    flattened = list(chain.from_iterable(matrix))
    return ''.join(flattened).count(to_count)

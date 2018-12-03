
from collections import Counter

from AoC2018.util import util


def count_twos_threes(line):
    """
    Counts the frequency of double and triple letters in a string.
    Return list: first element is true if some letters occur exactly 2 times
        and second element is true if some letters occur exactly 3 times.
    :param line: input line
    :return: list of 2 booleans
    """
    c = Counter(line).values()
    return [2 in c, 3 in c]


def calculate_checksum(lines):
    """
    Tally up all the results of the count_tows_threes and multiply them together.
    :param lines: input lines
    :return: integer checksum
    """
    twos = 0
    threes = 0
    for box in lines:
        counts = count_twos_threes(box)
        if counts[0]:
            twos += 1
        if counts[1]:
            threes += 1
    return twos * threes


@util.run_timer
def main():
    result = calculate_checksum(util.get_input_lines('input'))
    print(f'Checksum: {result}')


if __name__ == '__main__':
    main()

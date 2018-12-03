
from difflib import ndiff
from itertools import permutations

from AoC2018.util import util


def find_close_strings(lines):
    for to_compare in permutations(lines, 2):
        # generate sets of two in the permutations of all the lines
        s1 = to_compare[0]
        s2 = to_compare[1]
        # compare strings, only one character can be different between them
        if util.match_strings(s1, s2, not_matching=1):
            return [s1, s2]


@util.run_timer
def main():
    ids = util.get_input_lines('input')
    result = find_close_strings(ids)
    for line in ndiff([result[0]], [result[1]]):
        print(line.rstrip())


if __name__ == '__main__':
    main()

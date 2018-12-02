"""
/home/vance/PycharmProjects/AoC2018/venv/bin/python /home/vance/PycharmProjects/AoC2018/AoC2018/two/two_second.py
- qwugbihckpoymcpaxefotvdzns
? ^
+ jwugbihckpoymcpaxefotvdzns
? ^
runtime: 0.028927326202392578

Process finished with exit code 0
"""

from difflib import ndiff
from itertools import permutations

from AoC2018.day import day
from AoC2018.util import util


class Two(day.Day):
    def __init__(self):
        self.name = 'two'
        day.Day.__init__(self, self.name)

        self.input_lines = self.get_input_lines()

    @util.run_timer
    def main(self):

        for to_compare in permutations(self.input_lines, 2):
            # generate sets of two in the permutations of all the lines
            s1 = to_compare[0]
            s2 = to_compare[1]
            # compare strings, only one character can be different between them
            if util.match_strings(s1, s2, not_matching=1):
                for line in ndiff([s1], [s2]):
                    print(line.rstrip())
                # we only care about the first match (there's only one to find)
                break


if __name__ == '__main__':
    Two().main()

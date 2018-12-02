"""
$ python AoC2018/one/one.py
72330
loop count: 144
runtime: 0.04109048843383789
"""

from AoC2018.day import day
from AoC2018.util import util


class One(day.Day):
    def __init__(self):
        self.name = 'one'
        day.Day.__init__(self, self.name)

        self.input_lines = self.get_input_lines()
        self.frequency = 0
        self.frequencies = set()

    def calibrate_frequency(self):
        for drift in self.input_lines:
            self.frequency += int(drift)
            if self.frequency in self.frequencies:
                return True
            self.frequencies.add(self.frequency)

    @util.run_timer
    def main(self):
        self.frequencies.add(self.frequency) # add zero to the set

        loop_count = 0
        found = False
        while not found:
            found = self.calibrate_frequency()
            loop_count += 1

        print(f'frequency: {self.frequency}')
        print(f'loop count: {loop_count}')


if __name__ == '__main__':
    One().main()

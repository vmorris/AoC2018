"""
/home/vance/PycharmProjects/AoC2018/venv/bin/python /home/vance/PycharmProjects/AoC2018/AoC2018/two/two_first.py
Checksum: 7904
runtime: 0.0023674964904785156

Process finished with exit code 0
"""

from AoC2018.day import day
from AoC2018.util import util


class Two(day.Day):
    def __init__(self):
        self.name = 'two'
        day.Day.__init__(self, self.name)

        self.input_lines = self.get_input_lines()

        self.two_boxes = 0
        self.three_boxes = 0

    @util.run_timer
    def main(self):

        for box in self.input_lines:
            if util.check_frequency(box, 2):
                self.two_boxes += 1
            if util.check_frequency(box, 3):
                self.three_boxes += 1

        print(f'Checksum: {self.two_boxes * self.three_boxes}')


if __name__ == '__main__':
    Two().main()

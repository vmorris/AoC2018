import unittest

import AoC2018.three.three as three


class ThreeTests(unittest.TestCase):

    fabric = [['.'] * 8 for i in range(8)]

    inputs = ['#1 @ 1,3: 4x4',
              '#2 @ 3,1: 4x4',
              '#3 @ 5,5: 2x2']

    answer = [
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '2', '2', '2', '2', '.'],
        ['.', '.', '.', '2', '2', '2', '2', '.'],
        ['.', '1', '1', 'X', 'X', '2', '2', '.'],
        ['.', '1', '1', 'X', 'X', '2', '2', '.'],
        ['.', '1', '1', '1', '1', '3', '3', '.'],
        ['.', '1', '1', '1', '1', '3', '3', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.']
    ]

    def test_apply_rectangle(self):
        for line in self.inputs:
            self.fabric = three.apply_rectangle(self.fabric, line)
        self.assertEqual(self.fabric, self.answer)

    def test_count_overlap(self):
        self.assertEqual(4, three.count_overlap(self.answer))

    def test_check_intact(self):
        for claim in self.inputs:
            result = three.check_intact(self.answer, claim)
            if result:
                self.assertEqual('3', result)


if __name__ == '__main__':
    unittest.main()

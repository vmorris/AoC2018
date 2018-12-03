import unittest

import AoC2018.one.one as one


class OneTests(unittest.TestCase):

    input_1 = ['+1', '-2', '+3', '+1']
    input_2 = ['+1', '+1', '+1']
    input_3 = ['+1', '+1', '-2']
    input_4 = ['-1', '-2', '-3']

    def test_change_frequency(self):
        frequency = 0

        frequency = one.change_frequency(frequency, self.input_1[0])
        self.assertEqual(1, frequency)

        frequency = one.change_frequency(frequency, self.input_1[1])
        self.assertEqual(-1, frequency)

        frequency = one.change_frequency(frequency, self.input_1[2])
        self.assertEqual(2, frequency)

        frequency = one.change_frequency(frequency, self.input_1[3])
        self.assertEqual(3, frequency)

    def test_process_changes(self):
        result = one.process_changes(self.input_1)
        self.assertEqual(3, result)

        result = one.process_changes(self.input_2)
        self.assertEqual(3, result)

        result = one.process_changes(self.input_3)
        self.assertEqual(0, result)

        result = one.process_changes(self.input_4)
        self.assertEqual(-6, result)

    def test_find_duplicate(self):
        result = one.find_duplicate('+1, -1'.split(','))
        self.assertEqual(0, result)

        result = one.find_duplicate('+3, +3, +4, -2, -4'.split(','))
        self.assertEqual(10, result)

        result = one.find_duplicate('-6, +3, +8, +5, -6'.split(','))
        self.assertEqual(5, result)

        result = one.find_duplicate('+7, +7, -2, -7, -4'.split(','))
        self.assertEqual(14, result)


if __name__ == '__main__':
    unittest.main()

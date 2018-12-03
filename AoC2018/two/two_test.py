import unittest

import AoC2018.two.two_first as first
import AoC2018.two.two_second as second


class TwoTests(unittest.TestCase):

    boxes = ['abcdef',
             'bababc',
             'abbcde',
             'abcccd',
             'aabcdd',
             'abcdee',
             'ababab']

    ids = ['abcde',
           'fghij',
           'klmno',
           'pqrst',
           'fguij',
           'axcye',
           'wvxyz']

    def test_first_count_twos_threes(self):

        result = first.count_twos_threes(self.boxes[0])
        self.assertEqual([False, False], result)

        result = first.count_twos_threes(self.boxes[1])
        self.assertEqual([True, True], result)

        result = first.count_twos_threes(self.boxes[2])
        self.assertEqual([True, False], result)

        result = first.count_twos_threes(self.boxes[3])
        self.assertEqual([False, True], result)

        result = first.count_twos_threes(self.boxes[4])
        self.assertEqual([True, False], result)

        result = first.count_twos_threes(self.boxes[5])
        self.assertEqual([True, False], result)

        result = first.count_twos_threes(self.boxes[6])
        self.assertEqual([False, True], result)

    def test_first_calculate_checksum(self):

        result = first.calculate_checksum(self.boxes)
        self.assertEquals(12, result)

    def test_second_find_close_strings(self):

        result = second.find_close_strings(self.ids)
        self.assertEquals(['fghij', 'fguij'], result)


if __name__ == '__main__':
    unittest.main()
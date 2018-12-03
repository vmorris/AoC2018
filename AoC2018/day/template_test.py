import unittest

import AoC2018.day.template as template


class TemplateTests(unittest.TestCase):

    def test_placeholder(self):
        result = template.placeholder()
        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()
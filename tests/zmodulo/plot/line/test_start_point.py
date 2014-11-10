from unittest import TestCase
from zmodulo.plot.line.start_point import StartPoint

__author__ = 'aruff'


class TestArrow(TestCase):

    def test_integer_assignment(self):
        """
        Tests the integer initialization of the Arrow class
        """
        arrow = StartPoint(0, 0)
        self.assertEqual(arrow.to_str(), "\tx1 = 0;\n\ty1 = 0;\n")

    def test_string_assignment(self):
        """
        Tests the integer initialization of the Arrow class
        """
        arrow = StartPoint("0", "0")
        self.assertEqual(arrow.to_str(), "\tx1 = 0;\n\ty1 = 0;\n")

if __name__ == '__main__':
    TestCase.main()

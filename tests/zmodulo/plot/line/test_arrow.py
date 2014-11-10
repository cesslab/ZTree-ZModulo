from unittest import TestCase
from zmodulo.plot.line.arrow import Arrow

__author__ = 'aruff'


class TestArrow(TestCase):
    """
    Tester for the Z-Tree PlotLine Arrow class
    """
    def setUp(self):
        self.arrow = Arrow()

    def test_default_initialization(self):
        """
        Tests the default initialization of the Arrow class
        """
        self.assertEqual(self.arrow.to_str(), "\tarrowclosed = FALSE;\n")


if __name__ == '__main__':
    TestCase.main()

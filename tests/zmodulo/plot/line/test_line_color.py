from unittest import TestCase
from zmodulo.plot.line.line_color import LineColor
from zmodulo.plot.properties.color.color import Color

__author__ = 'aruff'


class TestLineColor(TestCase):

    def test_default_declaration_generation(self):
        """
        Tests the generation of a line color declaration with
        no parameters
        """
        line_color = LineColor()
        self.assertEqual(line_color.to_str(), "\tlinecolor = rgb(0.00,0.00,0.00);\n")

    def test_string_integer_value_declaration_generation(self):
        """
        Tests the generation of a line color declaration with
        string parameters
        """
        line_color = LineColor(Color("0", "0", "0"))
        self.assertEqual(line_color.to_str(), "\tlinecolor = rgb(0,0,0);\n")

    def test_string_named_value_declaration_generation(self):
        """
        Tests the generation of a line color declaration with
        string parameters
        """
        line_color = LineColor(Color("FOO", "BAR", "BAZ"))
        self.assertEqual(line_color.to_str(), "\tlinecolor = rgb(FOO,BAR,BAZ);\n")

if __name__ == '__main__':
    TestCase.main()

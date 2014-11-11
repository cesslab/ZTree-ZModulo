from unittest import TestCase
from zmodulo.plot.rectangle.fill_color import FillColor
from zmodulo.plot.properties.color.color import Color

__author__ = 'aruff'


class TestFillColor(TestCase):

    def test_default_declaration_generation(self):
        """
        Tests the generation of a fill color declaration with
        no parameters
        """
        fill_color = FillColor()
        self.assertEqual(fill_color.to_str(), "\tfillcolor = rgb(1.00,1.00,1.00);\n")

    def test_string_integer_value_declaration_generation(self):
        """
        Tests the generation of a fill color declaration with
        string parameters
        """
        fill_color = FillColor(Color("0", "0", "0"))
        self.assertEqual(fill_color.to_str(), "\tfillcolor = rgb(0,0,0);\n")

    def test_string_named_value_declaration_generation(self):
        """
        Tests the generation of a fill color declaration with
        string parameters
        """
        fill_color = FillColor(Color("FOO", "BAR", "BAZ"))
        self.assertEqual(fill_color.to_str(), "\tfillcolor = rgb(FOO,BAR,BAZ);\n")

if __name__ == '__main__':
    TestCase.main()

from unittest import TestCase
from zmodulo.plot.rectangle.rectangle_style import RectangleStyle
from zmodulo.plot.properties.color.color import Color
from zmodulo.plot.line.line_color import LineColor
from zmodulo.plot.line.line_width import LineWidth
from zmodulo.plot.rectangle.fill_color import FillColor

__author__ = 'aruff'


class TestRectangleStyle(TestCase):

    def test_default_declaration_generation(self):
        """
        Tests the generation of a rectangle style declaration with
        no parameters
        """
        line_style = RectangleStyle()
        self.assertEqual(line_style.to_str(),
                         "\tlinecolor = rgb(0.00,0.00,0.00);\n\tlinewidth = 1;\n\tfillcolor = rgb(1.00,1.00,1.00);\n")

    def test_string_integer_value_declaration_generation(self):
        """
        Tests the generation of a rectangle style declaration with
        string parameters
        """
        line_style = RectangleStyle(LineColor(Color(0, 0, 0)), LineWidth(2), FillColor(Color(0, 0, 0)))
        self.assertEqual(line_style.to_str(),
                         "\tlinecolor = rgb(0,0,0);\n\tlinewidth = 2;\n\tfillcolor = rgb(0,0,0);\n")

    def test_string_named_value_declaration_generation(self):
        """
        Tests the generation of a rectangle style declaration with
        string parameters
        """
        line_style = RectangleStyle(LineColor(
            Color("FOO", "BAR", "BAZ")), LineWidth("FOO"), FillColor(Color("BAZ", "BAR", "FOO")))
        self.assertEqual(line_style.to_str(),
                         "\tlinecolor = rgb(FOO,BAR,BAZ);\n\tlinewidth = FOO;\n\tfillcolor = rgb(BAZ,BAR,FOO);\n")

if __name__ == '__main__':
    TestCase.main()

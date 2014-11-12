from unittest import TestCase
from zmodulo.plot.text.text_color import TextColor
from zmodulo.plot.properties.color.color import Color

__author__ = 'aruff'


class TestTextColor(TestCase):

    def test_default_declaration_generation(self):
        """
        Tests the generation of a text color declaration with
        no parameters
        """
        text_color = TextColor()
        self.assertEqual(text_color.to_str(), "\ttextcolor = rgb(0.00,0.00,0.00);\n")

    def test_string_integer_value_declaration_generation(self):
        """
        Tests the generation of a text color declaration with
        string parameters
        """
        text_color = TextColor("0", "0", "0")
        self.assertEqual(text_color.to_str(), "\ttextcolor = rgb(0,0,0);\n")

    def test_string_named_value_declaration_generation(self):
        """
        Tests the generation of a text color declaration with
        string parameters
        """
        text_color = TextColor("FOO", "BAR", "BAZ")
        self.assertEqual(text_color.to_str(), "\ttextcolor = rgb(FOO,BAR,BAZ);\n")

if __name__ == '__main__':
    TestCase.main()

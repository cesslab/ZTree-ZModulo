from unittest import TestCase
from zmodulo.plot.properties.color.color import Color

__author__ = 'aruff'


class TestColor(TestCase):

    def test_default_declaration_generation(self):
        """
        Tests the generation of a color declaration with
        no parameters
        """
        color = Color()
        self.assertEqual(color.to_str(), "rgb(0.00,0.00,0.00)")

    def test_string_integer_value_declaration_generation(self):
        """
        Tests the generation of a color declaration with
        string parameters
        """
        color = Color("0", "0", "0")
        self.assertEqual(color.to_str(), "rgb(0,0,0)")

    def test_string_named_value_declaration_generation(self):
        """
        Tests the generation of a color declaration with
        string parameters
        """
        color = Color("FOO", "BAR", "BAZ")
        self.assertEqual(color.to_str(), "rgb(FOO,BAR,BAZ)")

if __name__ == '__main__':
    TestCase.main()


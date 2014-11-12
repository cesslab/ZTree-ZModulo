from unittest import TestCase
from zmodulo.plot.rectangle.rectangle_width import RectangleWidth

__author__ = 'aruff'


class TestRectangleWidth(TestCase):

    def test_default_declaration_generation(self):
        """
        Tests the generation of a rectangle width declaration with
        no parameters
        """
        rectangle_width = RectangleWidth()
        self.assertEqual(rectangle_width.to_str(), "\twidth = 10;\n")

    def test_string_integer_value_declaration_generation(self):
        """
        Tests the generation of a rectangle width declaration with
        string parameters
        """
        rectangle_width = RectangleWidth("1")
        self.assertEqual(rectangle_width.to_str(), "\twidth = 1;\n")

    def test_string_named_value_declaration_generation(self):
        """
        Tests the generation of a rectangle width declaration with
        string parameters
        """
        rectangle_width = RectangleWidth("FOO")
        self.assertEqual(rectangle_width.to_str(), "\twidth = FOO;\n")

if __name__ == '__main__':
    TestCase.main()

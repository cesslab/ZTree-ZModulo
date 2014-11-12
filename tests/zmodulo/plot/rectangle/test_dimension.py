from unittest import TestCase
from zmodulo.plot.rectangle.rectangle_dimension import RectangleDimension
from zmodulo.plot.rectangle.rectangle_width import RectangleWidth
from zmodulo.plot.rectangle.rectangle_height import RectangleHeight

__author__ = 'aruff'


class TestDimension(TestCase):

    def test_default_declaration_generation(self):
        """
        Tests the generation of a dimension declaration with no parameters
        """
        dimension = RectangleDimension()
        self.assertEqual(dimension.to_str(), "\twidth = 10;\n\theight = 10;\n")

    def test_string_integer_value_declaration_generation(self):
        """
        Tests the generation of a dimension declaration with string parameters
        """
        dimension = RectangleDimension("10", "10.01")
        self.assertEqual(dimension.to_str(), "\twidth = 10;\n\theight = 10.01;\n")

        dimension = RectangleDimension(RectangleWidth("10"), RectangleHeight("10.01"))
        self.assertEqual(dimension.to_str(), "\twidth = 10;\n\theight = 10.01;\n")

    def test_string_named_value_declaration_generation(self):
        """
        Tests the generation of a dimension declaration with string parameters
        """
        dimension = RectangleDimension(RectangleWidth("FOO"), RectangleHeight("BAR"))
        self.assertEqual(dimension.to_str(), "\twidth = FOO;\n\theight = BAR;\n")

if __name__ == '__main__':
    TestCase.main()


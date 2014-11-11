from unittest import TestCase
from zmodulo.plot.properties.coordinate import Coordinate

__author__ = 'aruff'


class TestCoordinate(TestCase):

    def test_default_declaration_generation(self):
        """
        Tests the generation of a coordinate declaration with
        no parameters
        """
        coordinate = Coordinate()
        self.assertEqual(coordinate.to_str(), "\tx = 0.0;\n\ty = 0.0;\n")

    def test_string_integer_value_declaration_generation(self):
        """
        Tests the generation of a coordinate declaration with
        string parameters
        """
        coordinate = Coordinate(1, 2)
        self.assertEqual(coordinate.to_str(), "\tx = 1;\n\ty = 2;\n")

    def test_string_named_value_declaration_generation(self):
        """
        Tests the generation of a coordinate declaration with
        string parameters
        """
        coordinate = Coordinate("FOO", "DOO")
        self.assertEqual(coordinate.to_str(), "\tx = FOO;\n\ty = DOO;\n")

if __name__ == '__main__':
    TestCase.main()


from unittest import TestCase
from zmodulo.plot.line.line_width import LineWidth

__author__ = 'aruff'


class TestLineWidth(TestCase):

    def test_default_declaration_generation(self):
        """
        Tests the generation of a line width declaration with
        no parameters
        """
        line_width = LineWidth()
        self.assertEqual(line_width.to_str(), "\tlinewidth = 1;\n")

    def test_string_integer_value_declaration_generation(self):
        """
        Tests the generation of a line width declaration with
        string parameters
        """
        line_width = LineWidth("1")
        self.assertEqual(line_width.to_str(), "\tlinewidth = 1;\n")

    def test_string_named_value_declaration_generation(self):
        """
        Tests the generation of a line width declaration with
        string parameters
        """
        line_width = LineWidth("FOO")
        self.assertEqual(line_width.to_str(), "\tlinewidth = FOO;\n")

if __name__ == '__main__':
    TestCase.main()

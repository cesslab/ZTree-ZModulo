from unittest import TestCase
from zmodulo.plot.text.font_type import FontType

__author__ = 'aruff'


class TestFontType(TestCase):
    """ Tester for the plot text FontType
    """

    def test_default_declaration_generation(self):
        """
        Tests the generation of a font type declaration with
        no parameters
        """
        font_type = FontType()
        self.assertEqual(font_type.to_str(), '\tfont = Arial;\n')

    def test_string_named_value_declaration_generation(self):
        """
        Tests the generation of a font type declaration with
        string parameters
        """
        font_type = FontType("Pooky")
        self.assertEqual(font_type.to_str(), '\tfont = Pooky;\n')

if __name__ == '__main__':
    TestCase.main()


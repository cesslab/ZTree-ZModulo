from unittest import TestCase
from zmodulo.plot.text.font_size import FontSize

__author__ = 'aruff'


class TestFontSize(TestCase):
    """ Tester for the plot text FontSize
    """

    def test_default_declaration_generation(self):
        """
        Tests the generation of a font size declaration with
        no parameters
        """
        font_size = FontSize()
        self.assertEqual(font_size.to_str(), '\tfontsize = 20;\n')

    def test_string_named_value_declaration_generation(self):
        """
        Tests the generation of a font size declaration with
        string parameters
        """
        font_size = FontSize("Pooky")
        self.assertEqual(font_size.to_str(), '\tfontsize = Pooky;\n')

if __name__ == '__main__':
    TestCase.main()


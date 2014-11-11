from unittest import TestCase
from zmodulo.plot.text.font_weight import FontWeight

__author__ = 'aruff'


class TestFontWeight(TestCase):
    """ Tester for the plot text FontWeight
    """

    def test_default_declaration_generation(self):
        """
        Tests the generation of a font weight declaration with
        no parameters
        """
        font_weight = FontWeight()
        self.assertEqual(font_weight.to_str(), '\tbold = FALSE;\n')

    def test_string_named_value_declaration_generation(self):
        """
        Tests the generation of a font weight declaration with
        string parameters
        """
        font_weight = FontWeight("Pooky")
        self.assertEqual(font_weight.to_str(), '\tbold = Pooky;\n')

if __name__ == '__main__':
    TestCase.main()


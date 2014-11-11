from unittest import TestCase
from zmodulo.plot.text.text import Text

__author__ = 'aruff'


class TestText(TestCase):
    """ Tester for the plot text Text
    """

    def test_default_declaration_generation(self):
        """
        Tests the generation of a font type declaration with
        no parameters
        """
        test = Text()
        self.assertEqual(test.to_str(), '\ttext = "";\n')

    def test_string_named_value_declaration_generation(self):
        """
        Tests the generation of a font type declaration with
        string parameters
        """
        test = Text("Pooky")
        self.assertEqual(test.to_str(), '\ttext = "Pooky";\n')

if __name__ == '__main__':
    TestCase.main()


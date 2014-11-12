from unittest import TestCase
from zmodulo.plot.text.text_style import TextStyle
from zmodulo.plot.text.text_color import TextColor
from zmodulo.plot.text.font_weight import FontWeight
from zmodulo.plot.text.font_size import FontSize
from zmodulo.plot.text.font_type import FontType
from zmodulo.plot.properties.color.color import Color

__author__ = 'aruff'


class TestTextStyle(TestCase):

    def test_default_declaration_generation(self):
        """
        Tests the generation of a text style declaration with no parameters
        """
        text_style = TextStyle()
        self.assertEqual(text_style.to_str(),
                         '\ttextcolor = rgb(0.00,0.00,0.00);\n\tfont = Arial;\n\tbold = FALSE;\n\tfontsize = 20;\n')

    def test_string_integer_value_declaration_generation(self):
        """
        Tests the generation of a text style declaration with string parameters
        """
        text_style = TextStyle(TextColor(0, 0, 0), FontSize(20), FontWeight(1),  FontType())
        self.assertEqual(text_style.to_str(),
                         '\ttextcolor = rgb(0,0,0);\n\tfont = Arial;\n\tbold = 1;\n\tfontsize = 20;\n')

    def test_string_named_value_declaration_generation(self):
        """
        Tests the generation of a text style declaration with string parameters
        """
        text_style = TextStyle(TextColor("Foo", "Baz", "Bin"), FontSize(20), FontWeight(1), FontType())
        self.assertEqual(text_style.to_str(),
                         "\ttextcolor = rgb(Foo,Baz,Bin);\n\tfont = Arial;\n\tbold = 1;\n\tfontsize = 20;\n")

if __name__ == '__main__':
    TestCase.main()

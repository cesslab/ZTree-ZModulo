from unittest import TestCase
from zmodulo.plot.line.line_style import LineStyle
from zmodulo.plot.line.line_color import LineColor
from zmodulo.plot.line.line_width import LineWidth
from zmodulo.plot.line.arrow import Arrow

__author__ = 'aruff'


class TestLineStyle(TestCase):

    def test_default_declaration_generation(self):
        """
        Tests the generation of a line style declaration with
        no parameters
        """
        line_style = LineStyle()
        line_color = LineColor()
        line_width = LineWidth()
        arrow = Arrow()
        self.assertEqual(
            line_style.to_str(), line_color.to_str()+line_width.to_str()+arrow.to_str())

if __name__ == '__main__':
    TestCase.main()

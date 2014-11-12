from unittest import TestCase
from zmodulo.plot.text.text_style import TextStyle
from zmodulo.plot.text.text import Text
from zmodulo.plot.text.text_color import TextColor
from zmodulo.plot.text.font_type import FontType
from zmodulo.plot.text.font_weight import FontWeight
from zmodulo.plot.text.font_size import FontSize
from zmodulo.plot.text.alignment import Alignment
from zmodulo.plot.text.plot_text import PlotText
from zmodulo.plot.properties.condition import Condition
from zmodulo.plot.properties.coordinate import Coordinate

__author__ = 'aruff'


class TestPlotText(TestCase):
    """ Tests the PlotText Template
    """

    def test_default_declaration_generation(self):
        """
        Tests the generation of a plot text declaration with no parameters
        """
        text = Text()
        color = TextColor()
        style = TextStyle()
        font_type = FontType()
        font_weight = FontWeight()
        font_size = FontSize()
        plot_text = PlotText()
        alignment = Alignment()
        coordinate = Coordinate()

        self.assertEqual(
            plot_text.to_str(),
            'plottext ""{\n' +
            text.to_str() + coordinate.to_str() + alignment.to_str() + color.to_str() +
            font_type.to_str() + font_weight.to_str() + font_size.to_str() + '}')

        condition = Condition("foo == doo")
        plot_text.condition = condition
        self.assertEqual(
            plot_text.to_str(),
            'plottext ""{\n' +
            condition.to_str() + text.to_str() + coordinate.to_str() + alignment.to_str() +
            style.to_str() + '}')

if __name__ == '__main__':
    TestCase.main()

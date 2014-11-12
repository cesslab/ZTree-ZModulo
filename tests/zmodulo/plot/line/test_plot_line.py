from unittest import TestCase
from zmodulo.plot.line.line_style import LineStyle
from zmodulo.plot.line.start_point import StartPoint
from zmodulo.plot.line.end_point import EndPoint
from zmodulo.plot.line.line_color import LineColor
from zmodulo.plot.line.line_width import LineWidth
from zmodulo.plot.line.plot_line import PlotLine
from zmodulo.plot.line.arrow import Arrow
from zmodulo.plot.properties.condition import Condition

__author__ = 'aruff'


class TestPlotLine(TestCase):
    """ Tests the PlotLine Template
    """

    def test_default_declaration_generation(self):
        """
        Tests the generation of a plot line declaration with no parameters
        """
        line_color = LineColor()
        line_width = LineWidth()
        start_point = StartPoint(0, 0)
        end_point = EndPoint(0, 1)
        line_style = LineStyle()
        plot_line = PlotLine(start_point, end_point)
        arrow = Arrow()
        self.assertEqual(
            plot_line.to_str(),
            'plotline ""{\n' +
            start_point.to_str() + end_point.to_str() + line_color.to_str() + line_width.to_str() + arrow.to_str()+'}')

        condition = Condition("foo == doo")
        plot_line.condition = condition
        self.assertEqual(
            plot_line.to_str(),
            'plotline ""{\n' +
            condition.to_str() + start_point.to_str() + end_point.to_str() + line_style.to_str() + '}')

if __name__ == '__main__':
    TestCase.main()

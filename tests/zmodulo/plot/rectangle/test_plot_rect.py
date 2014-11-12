from unittest import TestCase
from zmodulo.plot.properties.coordinate import Coordinate
from zmodulo.plot.properties.condition import Condition
from zmodulo.plot.rectangle.rectangle_dimension import RectangleDimension
from zmodulo.plot.rectangle.fill_color import FillColor
from zmodulo.plot.rectangle.plot_rect import PlotRect
from zmodulo.plot.rectangle.line_color import LineColor
from zmodulo.plot.rectangle.line_width import LineWidth
from zmodulo.plot.rectangle.rectangle_width import RectangleWidth
from zmodulo.plot.rectangle.rectangle_height import RectangleHeight

__author__ = 'aruff'


class TestPlotRect(TestCase):
    """ Tests the PlotRect Template
    """

    def test_default_declaration_generation(self):
        """
        Tests the generation of a plot line declaration with no parameters
        """
        coordinate = Coordinate()
        rect_width = RectangleWidth()
        rect_height = RectangleHeight()
        fill_color = FillColor()
        line_color = LineColor()
        line_width = LineWidth()

        plot_rect = PlotRect()
        self.assertEqual(
            plot_rect.to_str(),
            'plotrect ""{\n' + coordinate.to_str() + rect_width.to_str() + rect_height.to_str() +
            line_color.to_str() + line_width.to_str() + fill_color.to_str() + '}')

        condition = Condition("foo == baz")
        plot_rect.condition = condition
        self.assertEqual(
            plot_rect.to_str(),
            'plotrect ""{\n' + condition.to_str() + coordinate.to_str() + rect_width.to_str() + rect_height.to_str() +
            line_color.to_str() + line_width.to_str() + fill_color.to_str() + '}')

if __name__ == '__main__':
    TestCase.main()

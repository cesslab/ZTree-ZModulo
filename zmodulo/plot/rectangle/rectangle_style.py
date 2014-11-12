from zmodulo.plot.line.line_color import LineColor
from zmodulo.plot.rectangle.fill_color import FillColor
from zmodulo.plot.rectangle.line_width import LineWidth


class RectangleStyle:
    """ A Z-Tree Rectangle Style Template """

    def __init__(self, line_color=None, line_width=None, fill_color=None):
        """
        :param line_color: The rectangle line color
        :type line_color: LineColor
        :param line_width: The rectangle line width
        :type line_width: LineWidth
        :param fill_color: the rectangle fill color
        :type fill_color: FillColor
        """
        if line_color is None:
            self.line = LineColor()
        else:
            self.line = line_color

        if line_width is None:
            self.line_width = LineWidth()
        else:
            self.line_width = line_width

        if fill_color is None:
            self.fill_color = FillColor()
        else:
            self.fill_color = fill_color

        self.template = "{line_color}{line_width}{fill_color}"

    def to_str(self):
        """
        :return: The Z-Tree GUI Rectangle Style Assignment
        :rtype: str
        """
        return self.template.format(
            line_color=self.line.to_str(), line_width=self.line_width.to_str(), fill_color=self.fill_color.to_str())

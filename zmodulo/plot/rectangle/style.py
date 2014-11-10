from zmodulo.plot.line.line import Line
from zmodulo.plot.rectangle.fillcolor import FillColor


class Style:
    """ A Z-Tree Rectangle Style Template """

    def __init__(self, line=None, fill_color=None):
        """
        :param line: The rectangle line
        :type line: Line
        :param fill_color: the rectangle fill color
        :type fill_color: FillColor
        """
        if line is None:
            self.line = Line()
        else:
            self.line = line

        if fill_color is None:
            self.fill_color = FillColor()
        else:
            self.fill_color = fill_color

        self.template = "{line}{fill_color}"

    def to_str(self):
        """
        :return: The Z-Tree GUI Rectangle Style Assignment
        :rtype: str
        """
        return self.template.format(line=self.line.to_str(), fill_color=self.fill_color.to_str())

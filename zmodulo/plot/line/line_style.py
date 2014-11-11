from zmodulo.plot.line.line_color import LineColor
from zmodulo.plot.line.line_width import LineWidth
from zmodulo.plot.line.arrow import Arrow


class LineStyle:
    """ The Rectangle Style
    """

    def __init__(self, line_color=None, line_width=None, arrow_closed=None):
        """
        :param line_color: The line color
        :type line_color: Color
        :param line_width: The line width
        :type line_width: LineWidth
        :param arrow_closed: Arrow closed state
        :type arrow_closed: Arrow
        """
        if arrow_closed is None:
            self.arrow_closed = Arrow()
        else:
            self.arrow_closed = arrow_closed

        if line_color is None:
            self.line_color = LineColor()
        else:
            self.line_color = line_color

        if line_width is None:
            self.line_width = LineWidth()
        else:
            self.line_width = line_width

        self.template = "{line_color}{line_width}{arrow_closed}"

    def to_str(self):
        """
        Converts the line Style instance to a z-tree plot line property declarations
        :return: Z-Tree line style property declarations
        :rtype: str
        """
        return self.template.format(
            line_color=self.line_color.to_str(),
            line_width=self.line_width.to_str(),
            arrow_closed=self.arrow_closed.to_str())

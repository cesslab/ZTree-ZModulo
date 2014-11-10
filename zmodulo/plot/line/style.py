from zmodulo.plot.properties.color.color import Color


class Style:
    """ The Rectangle Style
    """

    def __init__(self, line_color=None, fill_color=None, line_width=1):
        """
        :param line_color: The line color
        :type line_color: Color
        :param fill_color: The fill color
        :type fill_color: Color
        :param line_width: The line width
        :type line_width: int
        """
        if fill_color is None:
            self.fill_color = Color()
        else:
            self.fill_color = fill_color

        if line_color is None:
            self.line_color = Color()
        else:
            self.line_color = line_color

        self.line_width = line_width

        self.template = "\tlinecolor = {line_color};\n\tlinewidth = {line_width};\n\tfillcolor = {fill_color}\n"

    def to_str(self):
        return self.template.format(
            line_color=self.line_color.get_str(), line_width=self.width, fill_color=self.fill_color)

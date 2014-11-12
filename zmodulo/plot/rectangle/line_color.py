from zmodulo.plot.properties.color.color import Color


class LineColor:
    """ A Z-Tree plot rectangle line color """

    def __init__(self, color=None):
        """
        Initializes the LineColor object
        :param color: line color
        :type color: Color
        """
        if color is None:
            self.color = Color()
        else:
            self.color = color

        self.template = '\tlinecolor = {line_color};\n'

    def to_str(self):
        """
        Converts the LineColor instance to a z-tree plot rectangle line color property declaration
        :return: Z-Tree linecolor property declaration
        :rtype: str
        """
        return self.template.format(line_color=self.color.to_str())


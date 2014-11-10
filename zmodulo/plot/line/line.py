from zmodulo.plot.line.style import Style
from zmodulo.plot.line.arrow import Arrow


class Line:
    """ The Z-tree Line Container
    """

    def __init__(self, style=None, arrow=None):
        """
        :param style: line style
        :type style: Style
        :param arrow: Arrow enabled
        :type arrow: Arrow
        """
        if style is None:
            self.style = Style()
        else:
            self.style = style

        if arrow is None:
            self.arrow = Arrow()
        else:
            self.arrow = arrow

        self.template = "{style}{arrow}"

    def to_str(self):
        return self.template.format(style=self.style.to_str(), arrow=self.arrow.to_str())

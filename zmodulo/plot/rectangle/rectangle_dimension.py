from zmodulo.plot.rectangle.rectangle_width import RectangleWidth
from zmodulo.plot.rectangle.rectangle_height import RectangleHeight


class RectangleDimension:
    """ A plot rectangle dimension template
    """
    def __init__(self, rectangle_width=None, rectangle_height=None):
        """
        Initialize the plot rectangle dimension
        :param rectangle_width: the plot rectangle width
        :param rectangle_height: the plot rectangle height
        """
        if rectangle_width is None:
            self.rectangle_width = RectangleWidth()
        elif isinstance(rectangle_width, RectangleWidth):
            self.rectangle_width = rectangle_width
        else:
            self.rectangle_width = RectangleWidth(rectangle_width)

        if rectangle_height is None:
            self.rectangle_height = RectangleHeight()
        elif isinstance(rectangle_height, RectangleHeight):
            self.rectangle_height = rectangle_height
        else:
            self.rectangle_height = RectangleHeight(rectangle_height)

        self.template = "{width}{height}"

    def to_str(self):
        return self.template.format(width=self.rectangle_width.to_str(), height=self.rectangle_height.to_str())

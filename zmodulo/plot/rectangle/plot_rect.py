from zmodulo.plot.rectangle.rectangle_dimension import RectangleDimension
from zmodulo.plot.properties.condition import Condition
from zmodulo.plot.properties.coordinate import Coordinate
from zmodulo.plot.rectangle.rectangle_style import RectangleStyle


class PlotRect:
    """ The Z-tree PlotRect Template """

    def __init__(self, position=None, dimension=None, style=None, condition=None, element_id=""):

        if position is None:
            self.position = Coordinate()
        else:
            self.position = position

        if dimension is None:
            self.dimension = RectangleDimension()
        else:
            self.dimension = dimension

        if style is None:
            self.rectangle_style = RectangleStyle()
        else:
            self.rectangle_style = style

        if condition is None:
            self.condition = Condition()
        else:
            self.condition = condition

        self.id = element_id

        self.template = 'plotrect "{id}"{{\n{body}}}'

    def to_str(self):
        """
        :return: z-tree plot entity string
        :rtype: str
        """
        return self.template.format(
            id=self.id,
            body=self.condition.to_str() + self.position.to_str() + self.dimension.to_str() +
            self.rectangle_style.to_str()
        )

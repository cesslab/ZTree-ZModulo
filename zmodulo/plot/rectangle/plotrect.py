from zmodulo.plot.rectangle.dimension import Dimension
from zmodulo.plot.properties.condition import Condition
from zmodulo.plot.properties.coordinate import Coordinate
from zmodulo.plot.rectangle.style import Style


class PlotRect:
    """ The Z-tree PlotRect Template """

    def __init__(self, position=None, dimension=None, style=None, condition=None, element_id=""):

        if position is None:
            self.position = Coordinate()
        else:
            self.position = position

        if dimension is None:
            self.dimension = Dimension()
        else:
            self.dimension = dimension

        if style is None:
            self.style = Style()
        else:
            self.style = style

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
            self.style.to_str()
        )

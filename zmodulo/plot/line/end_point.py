from zmodulo.plot.properties.coordinate import Coordinate


class EndPoint(Coordinate):
    """ A Z-Tree plot line end point
    """

    def __init__(self, x, y):
        """
        Initialize the plot line endpoint.

        :param x: x coordinate
        :type x: number
        :param y: y coordinate
        :type y: number
        """
        super().__init__(x, y, "x2", "y2")
        self.x = x
        self.y = y
from zmodulo.plot.properties.coordinate import Coordinate


class EndPoint(Coordinate):
    """ A plotline endpoint.
    """

    def __init__(self, x, y):
        """
        Initialize the plotline endpoint.
        :param x: x coordinate
        :type x: number
        :param y: y coordinate
        :type y: number
        """
        super().__init__(x, y, "x2", "y2")
        self.x = x
        self.y = y
from zmodulo.plot.properties.coordinate import Coordinate


class StartPoint(Coordinate):

    def __init__(self, x, y):
        super().__init__(x, y, "x1", "y1")
        self.x = x
        self.y = y
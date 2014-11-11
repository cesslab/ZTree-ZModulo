from zmodulo.plot.properties.color.color import Color
from zmodulo.plot.properties.color.white import White


class FillColor:
    """ Z-Tree Plot Rectangle Fill Color """

    def __init__(self, color=None):
        if color is None:
            self.color = Color(White.red, White.green, White.blue)
        else:
            self.color = color

        self.template = '\tfillcolor = {fillcolor};\n'

    def to_str(self):
        return self.template.format(fillcolor=self.color.to_str())


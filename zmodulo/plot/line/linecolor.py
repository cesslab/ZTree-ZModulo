from zmodulo.plot.properties.color.color import Color


class LineColor:
    """ Z-Tree Line Color Assignment Template """

    def __init__(self, color=None):
        if color is None:
            self.color = Color()
        else:
            self.color = color

        self.template = '\tlinecolor = {linecolor};\n'

    def to_str(self):
        return self.template.format(textcolor=self.color.to_str())


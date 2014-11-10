from zmodulo.plot.properties.color.color import Color


class TextColor:
    """ Z-Tree Plot Text Color """

    def __init__(self, color=None):
        if color is None:
            self.color = Color()
        else:
            self.color = color

        self.template = '\ttextcolor = {textcolor};\n'

    def to_str(self):
        return self.template.format(textcolor=self.color.to_str())


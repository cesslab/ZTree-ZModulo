from zmodulo.plot.text.fonttype import FontType
from zmodulo.plot.text.size import Size
from zmodulo.plot.text.weight import Weight
from zmodulo.plot.text.textcolor import TextColor


class Style:
    """ The Z-tree Font Contained """

    def __init__(self, color=None, weight=None, size=None, font_type=None):
        if color is None:
            self.color = TextColor()
        else:
            self.color = color

        if font_type is None:
            self.font_type = FontType()
        else:
            self.font_type = font_type

        if weight is None:
            self.weight = Weight()
        else:
            self.weight = weight

        if size is None:
            self.size = Size()
        else:
            self.size = size

        self.template = '{color}{font_type}{weight}{size}'

    def to_str(self):
        return self.template.format(
            color=self.color.to_str(),
            font_type=self.font_type.to_str(),
            weight=self.weight.to_str(),
            size=self.size.to_str()
        )

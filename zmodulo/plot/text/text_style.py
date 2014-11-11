from zmodulo.plot.text.font_type import FontType
from zmodulo.plot.text.font_size import FontSize
from zmodulo.plot.text.font_weight import FontWeight
from zmodulo.plot.text.text_color import TextColor


class TextStyle:
    """ The plot text style template
    """

    def __init__(self, color=None, weight=None, size=None, font_type=None):
        """
        :param color: text color
        :type color: TextColor
        :param weight: text weight
        :type weight:
        :param size:
        :type size:
        :param font_type:
        :type font_type:
        :return:
        :rtype:
        """
        if color is None:
            self.color = TextColor()
        else:
            self.color = color

        if font_type is None:
            self.font_type = FontType()
        else:
            self.font_type = font_type

        if weight is None:
            self.weight = FontWeight()
        else:
            self.weight = weight

        if size is None:
            self.size = FontSize()
        else:
            self.size = size

        self.template = '{color}{font_type}{weight}{size}'

    def to_str(self):
        """
        Converts the plot text font weight instance to a z-tree plot text weight property declaration.
        :return: plot text weight property declaration
        :rtype: str
        """
        return self.template.format(
            color=self.color.to_str(),
            font_type=self.font_type.to_str(),
            weight=self.weight.to_str(),
            size=self.size.to_str()
        )

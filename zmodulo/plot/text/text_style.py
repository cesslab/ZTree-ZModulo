from zmodulo.plot.text.font_type import FontType
from zmodulo.plot.text.font_size import FontSize
from zmodulo.plot.text.font_weight import FontWeight
from zmodulo.plot.text.text_color import TextColor


class TextStyle:
    """ The plot text style template
    """

    def __init__(self, color=None, font_size=None, font_weight=None, font_type=None):
        """
        :param color: text color
        :type color: TextColor
        :param font_size:
        :type font_size:
        :param font_weight: text weight
        :type font_weight:
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

        if font_weight is None:
            self.font_weight = FontWeight()
        else:
            self.font_weight = font_weight

        if font_size is None:
            self.font_size = FontSize()
        else:
            self.font_size = font_size

        self.template = '{text_color}{font_type}{font_weight}{font_size}'

    def to_str(self):
        """
        Converts the plot text style instance to a z-tree plot text style property declaration set.
        :return: plot text weight property declaration
        :rtype: str
        """
        return self.template.format(
            text_color=self.color.to_str(),
            font_type=self.font_type.to_str(),
            font_weight=self.font_weight.to_str(),
            font_size=self.font_size.to_str()
        )

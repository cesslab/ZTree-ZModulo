from zmodulo.plot.properties.color.color import Color
from zmodulo.plot.properties.color.black import Black



class TextColor:
    """ A Plot Text Text Color Template
    """

    def __init__(self, color=None):
        """
        Initialize the plot text text color instance
        :param color: text color
        :type color: Color
        """
        if color is None:
            self.color = Color(Black.red, Black.green, Black.blue)
        else:
            self.color = color

        self.template = '\ttextcolor = {textcolor};\n'

    def to_str(self):
        """
        Converts the plot text TextColor instance to a z-tree plot text text color property declaration.
        :return: plot text text color property declaration
        :rtype: str
        """
        return self.template.format(textcolor=self.color.to_str())


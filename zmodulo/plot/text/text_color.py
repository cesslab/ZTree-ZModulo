from zmodulo.plot.properties.color.color import Color
from zmodulo.plot.properties.color.black import Black


class TextColor:
    """ A Plot Text Text Color Template
    """

    def __init__(self, red=Black.red, green=Black.green, blue=Black.blue):
        """
        Initialize the plot text text color instance
        :param red: text red color percentage
        :param green: text green color percentage
        :param blue: text blue color percentage
        """
        self.color = Color(red, green, blue)

        self.template = '\ttextcolor = {textcolor};\n'

    def to_str(self):
        """
        Converts the plot text TextColor instance to a z-tree plot text text color property declaration.
        :return: plot text text color property declaration
        :rtype: str
        """
        return self.template.format(textcolor=self.color.to_str())


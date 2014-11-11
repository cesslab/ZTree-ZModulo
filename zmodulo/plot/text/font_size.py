class FontSize:
    """ The plot text font size template
    """
    LARGE = 30
    NORMAL = 20
    SMALL = 10

    def __init__(self, size=20):
        """
        Initializes the font size instance.
        :param size: text size
        :return:
        :rtype:
        """
        self.size = size
        self.template = '\tfontsize = {size};\n'

    def to_str(self):
        """
        Converts the font size instance to a Z-Tree plot text font size property declaration.
        :return: Z-Tree plot text font size declaration
        :rtype: str
        """
        return self.template.format(size=self.size)

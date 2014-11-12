class LineWidth:
    """ A plot rectangle line width """

    def __init__(self, width=1):
        """
        Initializes the LineWidth object
        :param width: line width
        """
        self.width = width

        self.template = '\tlinewidth = {width};\n'

    def to_str(self):
        """
        Converts the LineWidth instance to a z-tree plot rectangle property declaration
        :return: Z-Tree line width property declaration
        :rtype: str
        """
        return self.template.format(width=self.width)


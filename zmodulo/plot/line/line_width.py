class LineWidth:
    """ A Z-Tree plot line width """

    def __init__(self, width=1):
        """
        Initializes the LineWidth object
        :param width: line width
        """
        self.width = width

        self.template = '\tlinewidth = {width};\n'

    def to_str(self):
        """
        Converts the LineWidth instance to a z-tree plot line property declaration
        :return: Z-Tree line width property declaration
        :rtype: str
        """
        return self.template.format(width=self.width)


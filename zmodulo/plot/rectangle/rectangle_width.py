class RectangleWidth:
    """ A Z-Tree plot rectangle width """

    def __init__(self, width=10):
        """
        Initializes the RectangleWidth object
        :param width: rectangle width
        """
        self.width = width

        self.template = '\twidth = {width};\n'

    def to_str(self):
        """
        Converts the RectangleWidth instance to a plot rectangle width property declaration
        :return: plot rectangle width property declaration
        :rtype: str
        """
        return self.template.format(width=self.width)


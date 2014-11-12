class RectangleHeight:
    """ A Z-Tree plot rectangle height """

    def __init__(self, height=10):
        """
        Initializes the RectangleHeight object
        :param height: rectangle height
        """
        self.height = height

        self.template = '\theight = {height};\n'

    def to_str(self):
        """
        Converts the RectangleHeight instance to a plot rectangle height property declaration
        :return: plot rectangle height property declaration
        :rtype: str
        """
        return self.template.format(height=self.height)


class Coordinate:
    """ A Z-Tree plot coordinate
    """

    def __init__(self, x=0.00, y=0.00, x_id="x", y_id="y"):
        """
        :param x: x coordinate
        :param y: y coordinate
        :param x_id: x coordinate id
        :type x_id: str
        :param y_id: y coordinate id
        :type y_id: str
        :return:
        :rtype:
        """
        self.x = x
        self.y = y
        self.x_id = x_id
        self.y_id = y_id
        self.template = '\t{} = {};\n\t{} = {};\n'

    def to_str(self):
        """
        Converts the coordinate object to a z-tree plot coordinate declaration
        :return: z-tree coordinate declaration
        :rtype: str
        """
        return self.template.format(self.x_id, str(self.x), str(self.y_id), str(self.y))


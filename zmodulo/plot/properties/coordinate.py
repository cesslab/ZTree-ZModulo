class Coordinate:
    """ A plot coordinate
    """

    def __init__(self, x=0.00, y=0.00, x_id="x", y_id="y"):
        self.x = x
        self.y = y
        self.x_id = x_id
        self.y_id = y_id
        self.template = '\t{} = {};\n\t{} = {};\n'

    def to_str(self):
        return self.template.format(self.x_id, str(self.x), str(self.y_id), str(self.y))


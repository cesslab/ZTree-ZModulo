class Dimension:
    """ The Z-tree Dimension Container
    """
    def __init__(self, height=10.00, width=10.00):
        self.height = height
        self.width = width
        self.template = "\twidth = {width};\n\theight = {height};\n"

    def to_str(self):
        return self.template.format(width="{:.2f}".format(self.width), height="{:.2f}".format(self.height))

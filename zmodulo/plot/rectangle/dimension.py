class Dimension:
    """ The Z-tree Dimension Container
    """
    def __init__(self, width=10, height=10):
        self.height = height
        self.width = width
        self.template = "\twidth = {width};\n\theight = {height};\n"

    def to_str(self):
        return self.template.format(width=self.width, height=self.height)

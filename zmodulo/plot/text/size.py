class Size:
    """ The Z-Tree Font Size Template
    """
    LARGE = "30"
    NORMAL = "20"
    SMALL = "10"

    def __init__(self, size="20"):
        self.size = size
        self.template = '\tfontsize = {size};\n'

    def to_str(self):
        """
        :return: formatted Z-Tree text size
        :rtype: str
        """
        return self.template.format(size=self.size)

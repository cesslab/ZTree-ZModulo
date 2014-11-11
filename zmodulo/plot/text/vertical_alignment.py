class VerticalAlignment():
    """ The Plot Text Vertical Alignment Template
    """
    center = "CENTER"
    top = "TOP"
    bottom = "BOTTOM"

    def __init__(self, alignment="CENTER"):
        """
        Initializes the VerticalAlignment instance
        :param alignment: The plot text vertical alignment
        :type alignment: str
        """
        self.alignment = alignment

        self.template = '\tverticalalignment = {alignment};\n'

    def to_str(self):
        """
        Converts the plot text vertical alignment instance to a z-tree vertical alignment property declaration.
        :return: plot text horizontal alignment property declaration
        :rtype: str
        """
        return self.template.format(alignment=self.alignment)

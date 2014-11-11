class HorizontalAlignment():
    """ The Plot Text Horizontal Alignment Template
    """
    center = "CENTER"
    left = "LEFT"
    right = "RIGHT"

    def __init__(self, alignment="CENTER"):
        """
        Initializes the HorizontalAlignment instance
        :param alignment: The plot text horizontal alignment
        :type alignment: str
        """
        self.alignment = alignment

        self.template = '\thorizontalalignment = {alignment};\n'

    def to_str(self):
        """
        Converts the plot text horizontal alignment instance to a z-tree horizontal alignment property declaration.
        :return: plot text horizontal alignment property declaration
        :rtype: str
        """
        return self.template.format(alignment=self.alignment)


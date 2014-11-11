class FontWeight:
    """ The plot text font weight template
    """

    NORMAL = "FALSE"
    BOLD = "TRUE"

    def __init__(self, weight="FALSE"):
        """
        Initializes the FontWeight instance.
        :param weight: plot text font weight
        :type weight: str
        """
        self.weight = weight

        self.template = '\tbold = {weight};\n'

    def to_str(self):
        """
        Converts the plot text font weight instance to a z-tree plot text weight property declaration.
        :return: plot text weight property declaration
        :rtype: str
        """
        return self.template.format(weight=self.weight)

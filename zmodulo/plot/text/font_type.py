class FontType:
    """ The Z-Tree Font Type Template
    """

    ARIAL = "Arial"

    def __init__(self, font_type="Arial"):
        """
        :param font_type: The text type
        :type font_type: str
        """
        self.font_type = font_type

        self.template = '\tfont = {font_type};\n'

    def to_str(self):
        """
        :return: formatted Z-Tree text type
        :rtype: str
        """
        return self.template.format(font_type=self.font_type)

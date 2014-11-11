class Text:
    """ The Plot Text Text Template
    """

    def __init__(self, text=""):
        """
        Initializes the plot text Text
        :param text: plot text text
        :type text: str
        """
        self.text = text
        self.template = '\ttext = "{text}";\n'

    def to_str(self):
        """
        Converts the plot text text instance to a z-tree text property declaration.
        :return: plot text text property declaration
        :rtype: str
        """
        return self.template.format(text=self.text)

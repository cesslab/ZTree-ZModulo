class Arrow:
    """
    The Z-Tree Line Arrow Property
    """

    ENABLED = "TRUE"
    DISABLED = "FALSE"

    def __init__(self, enabled=None):
        """
        Initializes the Arrow object
        :param enabled: determines if the arrow is enabled "TRUE" or "FALSE"
        :type enabled: str
        """
        if enabled is None:
            self.enabled = "FALSE"
        else:
            self.enabled = enabled

        self.template = "\tarrowclosed = {enabled};\n"

    def to_str(self):
        """
        :return: Z-Tree arrowclosed property assignment
        :rtype: str
        """
        return self.template.format(enabled=self.enabled)


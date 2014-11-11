class Color:
    """ The Z-tree Color Container"""

    def __init__(self, red="0.00", green="0.00", blue="0.00"):
        """
        :param red: Red value or variable name
        :type red: str
        :param green: green or variable name
        :type green: str
        :param blue: blue or variable name
        :type blue: str
        """
        self.red = red
        self.green = green
        self.blue = blue

        self.template = 'rgb({red},{green},{blue})'

    def to_str(self):
        return self.template.format(red=str(self.red), green=str(self.green), blue=str(self.blue))


from zmodulo.plot.text.horizontal import Horizontal
from zmodulo.plot.text.vertical import Vertical


class Alignment:
    """ The Z-tree Alignment Container """

    def __init__(self):
        self.horizontal = Horizontal.center.value
        self.vertical = Vertical.center.value
        self.template = '\thorizontalalignment = {horizontal};\n\tverticalalignment = {vertical};\n'

    def to_str(self):
        return self.template.format(horizontal=self.horizontal, vertical=self.vertical)

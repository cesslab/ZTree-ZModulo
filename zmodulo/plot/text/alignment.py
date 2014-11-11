from zmodulo.plot.text.horizontal_alignment import HorizontalAlignment
from zmodulo.plot.text.vertical_alignment import VerticalAlignment


class Alignment:
    """ The Z-tree Plot Text Alignment Template """

    def __init__(self, horizontal_alignment=None, vertical_alignment=None):
        """
        Initializes the Alignment instance
        :param horizontal_alignment: Plot Text horizontal alignment property
        :type horizontal_alignment: HorizontalAlignment
        :param vertical_alignment: Plot Text vertical alignment property
        :type vertical_alignment: VerticalAlignment
        """
        if horizontal_alignment is None:
            self.horizontal_alignment = HorizontalAlignment()
        else:
            self.horizontal_alignment = horizontal_alignment

        if vertical_alignment is None:
            self.vertical_alignment = VerticalAlignment()
        else:
            self.vertical_alignment = vertical_alignment

        self.template = '{horizontal_alignment}{vertical_alignment}'

    def to_str(self):
        """
        Converts the alignment instance to a z-tree plot line property declaration.
        :return: Z-Tree alignment property assignment
        :rtype: str
        """
        return self.template.format(
            horizontal_alignment=self.horizontal_alignment.to_str(),
            vertical_alignment=self.vertical_alignment.to_str()
        )

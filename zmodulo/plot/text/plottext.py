from zmodulo.plot.properties.coordinate import Coordinate
from zmodulo.plot.text.alignment import Alignment
from zmodulo.plot.text.style import Style
from zmodulo.plot.properties.condition import Condition
from zmodulo.plot.text.text import Text


class PlotText():
    def __init__(self, element_id="", condition=None, text=None, position=None, alignment=None,
                 font=None):
        """
        :param element_id: z-tree element id
        :type element_id: str
        :param condition: plot text display condition
        :type condition: Condition
        :param text: text displayed in the plot text
        :type text: Text
        :param position: the coordinate the text will be plotted on
        :type position: Coordinate
        :param alignment: the text alignment
        :type alignment: Alignment
        :param font: the text the text is rendered in
        :type font: Style
        """
        self.id = element_id

        if condition is None:
            self.condition = Condition()
        else:
            self.condition = condition

        if text is None:
            self.text = Text()
        else:
            self.text = text

        if position is None:
            self.position = Coordinate()
        else:
            self.position = position

        if alignment is None:
            self.alignment = Alignment()
        else:
            self.alignment = alignment

        if font is None:
            self.font = Style()
        else:
            self.font = font

        self.template = 'plottext "{}"{{\n{}}}'

    def to_str(self):
        """
        :return: z-tree plot entity string
        :rtype: str
        """
        condition = self.condition.to_str()
        text = self.text.to_str()
        position = self.position.to_str()
        alignment = self.alignment.to_str()
        font = self.font.to_str()

        return self.template.format(self.id, condition + text + position + alignment + font)

from unittest import TestCase
from zmodulo.plot.text.alignment import Alignment
from zmodulo.plot.text.vertical_alignment import VerticalAlignment
from zmodulo.plot.text.horizontal_alignment import HorizontalAlignment

__author__ = 'aruff'


class TestAlignment(TestCase):

    def test_default_declaration_generation(self):
        """ Tests the generation of an alignment declaration with no parameters
        """
        alignment = Alignment()
        self.assertEqual(alignment.to_str(),
                         '\thorizontalalignment = CENTER;\n\tverticalalignment = CENTER;\n')

    def test_string_named_value_declaration_generation(self):
        """ Tests the generation of an alignment declaration with string parameters
        """
        alignment = Alignment(HorizontalAlignment("LEFT"), VerticalAlignment("TOP"))
        self.assertEqual(alignment.to_str(),
                         '\thorizontalalignment = LEFT;\n\tverticalalignment = TOP;\n')

        alignment.horizontal_alignment = HorizontalAlignment(HorizontalAlignment.center)
        alignment.vertical_alignment = VerticalAlignment(VerticalAlignment.top)
        self.assertEqual(alignment.to_str(),
                         '\thorizontalalignment = CENTER;\n\tverticalalignment = TOP;\n')

if __name__ == '__main__':
    TestCase.main()


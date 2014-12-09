from unittest import TestCase

from zmodulo.collections.table import Table

__author__ = 'aruff'


class TestTable(TestCase):
    def test_find(self):
        table = Table("TestTable")
        self.assertEqual(table.find("Same(Subject)", "someVar"),
                         'TestTable.find(Same(Subject), someVar)')

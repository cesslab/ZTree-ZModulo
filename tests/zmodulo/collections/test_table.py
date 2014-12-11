from unittest import TestCase

from zmodulo.collections.table import Table

__author__ = 'aruff'


class TestTable(TestCase):
    def test_find(self):
        table = Table("TestTable")
        self.assertEqual(table.find('someVar'), 'TestTable.find(someVar)')
        self.assertEqual(table.filter_find(table.same('Subject'), 'someVar'), 'TestTable.find(Same(Subject), someVar)')

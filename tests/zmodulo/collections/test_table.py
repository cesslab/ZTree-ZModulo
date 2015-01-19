from unittest import TestCase

from zmodulo.collections.table import Table

__author__ = 'aruff'


class TestTable(TestCase):
    def test_find(self):
        table = Table("TestTable")
        self.assertEqual("TestTable.find(Table("TestTable").same('Subject').filter('Round', '==', '2').find('var'))
        self.assertEqual(table.find('someVar'), 'TestTable.find(someVar)')
        self.assertEqual(table.filtered_find('p == q & foo = bar', 'someVar'), 'TestTable.find(Same(Subject), someVar)')
        self.assertEqual(table.filtered_find_same(table.same('Subject'), 'someVar'), 'TestTable.find(Same(Subject), someVar)')

from unittest import TestCase

from zmodulo.operators.Logic import Logic


class TestLogic(TestCase):
    def test_and(self):
        self.assertEqual(' & p == q', Logic.and_equals('p', 'q'))
        self.assertEqual(' & p == {q}', Logic.and_equals('p', '{q}'))



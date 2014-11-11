from unittest import TestCase
from zmodulo.plot.properties.condition import Condition

__author__ = 'aruff'


class TestCondition(TestCase):

    def test_default_declaration_generation(self):
        """
        Tests the generation of a condition declaration with
        no parameters
        """
        condition = Condition()
        self.assertEqual(condition.to_str(), "")

    def test_string_integer_value_declaration_generation(self):
        """
        Tests the generation of a condition declaration with
        string parameters
        """
        condition = Condition("1")
        self.assertEqual(condition.to_str(), "\tdisplaycondition = 1;\n")

    def test_string_named_value_declaration_generation(self):
        """
        Tests the generation of a condition declaration with
        string parameters
        """
        condition = Condition("FOO")
        self.assertEqual(condition.to_str(), "\tdisplaycondition = FOO;\n")
        condition.predicate = "FOO != DOO"
        self.assertEqual(condition.to_str(), "\tdisplaycondition = FOO != DOO;\n")

if __name__ == '__main__':
    TestCase.main()


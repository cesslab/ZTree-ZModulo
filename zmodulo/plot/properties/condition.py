class Condition:
    """ A Z-Tree Plot Condition """

    def __init__(self, predicate=""):
        """
        :param predicate: z-tree plot predicate
        :type predicate: str
        """
        self.predicate = predicate
        self.template = '\tdisplaycondition = {predicate};\n'

    def to_str(self):
        """
        Converts the condition to a z-tree condition property declaration.
        :return: Z-Tree condition property assignment
        :rtype: str
        """
        if not self.predicate:
            return ""

        return self.template.format(predicate=self.predicate)

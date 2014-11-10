class Condition:

    def __init__(self, predicate=""):
        """
        :param predicate: z-tree plot entity display condition
        :type predicate: str
        """
        self.predicate = predicate
        self.template = '\tdisplaycondition = {predicate};\n'

    def to_str(self):
        if not self.predicate:
            return ""

        return self.template.format(predicate=self.predicate)

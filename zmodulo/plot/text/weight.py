class Weight:

    NORMAL = "FALSE"
    BOLD = "TRUE"

    def __init__(self, weight="FALSE"):
        self.weight = weight

        self.template = '\tbold = {weight};\n'

    def to_str(self):
        return self.template.format(weight=self.weight)

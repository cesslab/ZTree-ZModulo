class Text:

    def __init__(self, text=""):
        self.text = text
        self.template = '\ttext = "{text}";\n'

    def to_str(self):
        return self.template.format(text=self.text)

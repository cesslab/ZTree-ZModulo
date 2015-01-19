class Table:
    """ The Table template
    """

    def __init__(self, name):
        """
        :param name: table name
        :type name: str
        """
        self.name = name
        self.find_var = ""
        self.find_filter = ""
        self.find_template = ".find({})"
        self.str = ""

    def filter_find(self, find_filter, find_var):
        """
        :param find_filter: z-tree filter
        :type find_filter: str
        :param find_var: z-tree var to find in the table
        :type find_var: str
        :return: find string
        :rtype: str
        """
        find_template = self.name + self.find_template.format('{}, {}')
        return find_template.format(find_filter, find_var)

    def find(self, find_var):
        """
        :param find_var: z-tree var to find in the table
        :type find_var: str
        :return: find string
        :rtype: str
        """
        find_template = self.name + '.find({v})'
        return find_template.format(v=find_var)

    @staticmethod
    def same(var_name):
        """
        :param var_name: variable name
        :type var_name: str
        :return: find string
        :rtype: str
        """
        return "Same({})".format(var_name)
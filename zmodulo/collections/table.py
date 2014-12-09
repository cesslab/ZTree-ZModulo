class Table:
    """ The Table template
    """

    def __init__(self, name):
        """
        :param name: table name
        :type name: str
        """
        self.name = name

    def find(self, find_filter, find_var):
        """
        :param find_filter: z-tree filter
        :type find_filter: str
        :param find_var: z-tree var to find in the table
        :type find_var: str
        :return: find string
        :rtype: str
        """
        find_template = self.name + '.find({f}, {v})'
        return find_template.format(f=find_filter, v=find_var)
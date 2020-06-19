

class Category:

    """
        Default constructor for user class

        Parameters
        ------------------------------------
        info: contains [name of category, time period of budget
                        target of the budget]
    """
    def __init__(self, info):
        self.name = info[0]
        self.period = info[1]
        self.target = info[2]
        self.balance = 0        # Will start off as 0 as default
        self.labels = []        # Labels should be empty, since it will be 
                                # added onto as user sifts through transactions




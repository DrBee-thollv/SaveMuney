

class BankAcc:

    """
        Default constructor for user class

        Parameters
        ------------------------------------
        username: username to set the users account to
    """
    def __init__(self, LogIn, URL):
        self.username = LogIn[0]
        self.password = LogIn[1]
        self.url = URL
        self.statements = []
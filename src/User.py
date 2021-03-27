
from BankAcc import BankAcc
from Category import Category

class User:
    """Default constructor for user class

    Parameters
    ------------------------------------
    username : str
        username to set the users account to
    """
    def __init__(self, username):
        self.bank = BankAcc()
        self.categories = []
        self.username = username
        print("You have created a user named: ", username)


    def SetBank(self, LogIn, URL):
        """Setter for users Bank Account 

        Parameters
        ------------------------------------
        LogIn : str
            List containing username and password for users' bank acc

        URL : str
            web link leading to the users bank
        """
        self.bank = BankAcc(LogIn, URL)


    def GetBank():
        """Getter for users bank class instance

        Return
        ------------------------------------
            returns instance of users bank
        """
        return self.bank


    def SetUsername(self, username):
        """Setter for users username

        Parameters
        ------------------------------------
        username : str
            The username to be assigned
        """
        self.username = username
    

    def GetUsername():
        """Getter for the users username

        Return
        ------------------------------------
            returns string of users username
        """
        return self.username


    def AddCategory(self, info):
        """Appends a new instance of category to the users account

        Parameters
        ------------------------------------
        info : 
            a list containing the parameters to set the new category being added
        """
        self.categories.append(Category(info))


    def RemoveCategory(self, name):
        """Removes instance of category from users account

        Parameters
        ------------------------------------
        name : str
            The name of the category to delete
        """
        # self.categories.remove(cat) for cat in self.categories if name == cat.name
        for cat in self.categories:
            if(name == cat.name):
                self.categories.remove(cat)
                print("Category: " + name + " was removed.")
        print("Category: " + name + " could not be removed.")



    

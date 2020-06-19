
from BankAcc import BankAcc
from Category import Category

class User:
    """
        Default constructor for user class

        Parameters
        ------------------------------------
        username: username to set the users account to
    """
    def __init__(self, username):
        self.bank = BankAcc()
        self.categories = []
        self.username = username
        print("You have created a user named: ", username)


    """
        Setter for users Bank Account 

        Parameters
        ------------------------------------
        LogIn: List containing username and password for users' bank acc
        URL: web link leading to the users bank
    """
    def SetBank(self, LogIn, URL):
        self.bank = BankAcc(LogIn, URL)


    """
        Getter for users bank class instance

        Return
        ------------------------------------
        returns instance of users bank
    """
    def GetBank():
        return self.bank


    """
        Setter for users username

        Parameters
        ------------------------------------
        username: The username to be assigned
    """
    def SetUsername(self, username):
        self.username = username
    

    """
        Getter for the users username

        Return
        ------------------------------------
        returns string of users username
    """
    def GetUsername():
        return self.username


    """
        Appends a new instance of category to the users account

        Parameters
        ------------------------------------
        info: a list containing the parameters to set the new category being added
    """
    def AddCategory(self, info):
        self.categories.append(Category(info))


    """
        Removes instance of category from users account

        Parameters
        ------------------------------------
        name: The name of the category to delete
    """
    def RemoveCategory(self, name):
        for cat in self.categories:
            if(name == cat.name):
                self.categories.remove(cat)
                print("Category: " + name + " was removed.")
        print("Category: " + name + " could not be removed.")



    

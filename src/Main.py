from User import User


kalia = User("Kalia")

while(1):
    print(kalia.categories)
    hai = input("Do you wanna add a class?")
    
    if(hai == "y"):
        name = input("What is tha name of the cat you wanna add bro?")
        period = input("What is the period of this cat (0-week, 1-month, 2-year): ")
        target = input("What is the target balance of your thingy: ")
        info = [name, period, target]
        kalia.AddCategory(info)
    elif(hai == "n"):
        name = input("What is da name of the cat: ")
        kalia.RemoveCategory(name)
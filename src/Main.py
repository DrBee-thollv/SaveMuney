from User import User

"""
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
"""
import kivy
kivy.require('1.10.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LogIn(FloatLayout):
    def ShowTextBoxes(self):
        turn_off = [self.ids['New'], self.ids['Existing']]
        turn_on = self.ids['Back']
        turn_on.opacity = 1
        turn_on.disabled = False
        for switch in turn_off:
            switch.opacity = 0
            switch.disabled = True

    def ShowFirstLogIn(self):
        turn_on = [self.ids['New'], self.ids['Existing']]
        turn_off = self.ids['Back']
        turn_off.disabled = True
        turn_off.opacity = 0
        for switch in turn_on:
            switch.opacity = 1
            switch.disabled = False

class SaveMuneyApp(App):

    def build(self):
        self.load_kv("SaveMuney.kv")
        return LogIn()


if __name__ == '__main__':
    SaveMuneyApp().run()

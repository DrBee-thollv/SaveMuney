from User import User
import kivy
kivy.require('1.10.1') # replace with your current kivy version !

from kivy.app import App
from kivy.app import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class NewUser(Screen):
    pass

class ExistingUser(Screen):
    pass

class LogIn(Screen):
    pass

class SaveMuneyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LogIn(name="login"))
        sm.add_widget(NewUser(name="new"))
        sm.add_widget(ExistingUser(name="existing"))

        return sm

if __name__ == '__main__':
    SaveMuneyApp().run()

import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.behaviors.focus import FocusBehavior
from kivy.properties import NumericProperty, ObjectProperty
from kivy.lang.builder import Builder

from os import listdir

PATH = './kv/'
for kv in listdir(PATH):
    Builder.load_file(PATH + kv)


class HomeScreen(FloatLayout):
    first_name = ObjectProperty()
    last_name = ObjectProperty()
    prisoner_number = ObjectProperty()
    institution = ObjectProperty()
    address_one = ObjectProperty()
    address_two = ObjectProperty()
    city = ObjectProperty()
    state = ObjectProperty()
    zipcode = ObjectProperty()

    def clear_fields(self):
        self.first_name.text = ""
        self.last_name.text = ""
        self.prisoner_number.text = ""
        self.institution.text = ""
        self.address_one.text = ""
        self.address_two.text = ""
        self.city.text = ""
        self.state.text = ""
        self.zipcode.text = ""

    def print_fields(self):
        print("The first name is: {text}.".format(text=self.first_name.text))


class CustomDropDown(BoxLayout):
    pass


class LeftLabel(Label):
    halign = 'left'
    valign = 'middle'


class PlaceHolder(Label):
    pass


class OneLineInput(TextInput):
    multiline = False


class MenuTab(TabbedPanel):
    pass


class MyApp(App):
    title = 'Letter Writer'

    def build(self):
        return HomeScreen()


if __name__ == '__main__':
    MyApp().run()

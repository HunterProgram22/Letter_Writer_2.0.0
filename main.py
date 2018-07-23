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
#from kivy.properties import NumericProperty, ObjectProperty
from kivy.lang.builder import Builder

from os import listdir

PATH = './kv/'
for kv in listdir(PATH):
    Builder.load_file(PATH + kv)


class HomeScreen(FloatLayout):
    pass


class LeftLabel(Label):
    halign = 'left'
    valign = 'middle'


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

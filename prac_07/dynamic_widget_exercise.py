"""
CP1404 prac_07.dynamic_widget_exercise.py by Christopher Caferra
Kivy GUI program to test dynamic widgets.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetExerciseApp(App):
    """ DynamicWidgetExerciseApp is a kivy app for testing dynamic widgets. """

    names = ["Chris", "Bob", "Kathy", "Julie", "Holly", "Dave"]

    def build(self):
        """ Build the kivy app from the .kv file and call create_widget function"""
        self.title = 'Dynamic Widgets'
        self.root = Builder.load_file('dynamic_widget_exercise.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """ Create widget and add to label_output ids. """
        for name in self.names:
            name_label = Label(text=name)
            self.root.ids.label_output.add_widget(name_label)


DynamicWidgetExerciseApp().run()

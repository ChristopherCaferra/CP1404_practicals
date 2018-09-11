"""
CP1404 prac_07.convert_m_km.py by Christopher Caferra
Kivy GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesToKilometresApp(App):

    def build(self):
        Window.size = (400, 200)
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root

    def handle_conversion_calculation(self, value):
        result = value * 1.609
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, value, increment):
        result = value + increment
        self.root.ids.input_number.text = str(result)


ConvertMilesToKilometresApp().run()

"""
CP1404 prac_07.convert_m_km.py by Christopher Caferra
Kivy GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesToKilometresApp(App):
    """ ConvertMilesToKilometresApp is a Kivy App for converting miles to kilometres. """
    MILES_TO_KM = 1.60934

    def build(self):
        """ Build the Kivy app from the kv file. """
        Window.size = (400, 200)
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root

    def handle_calculate_conversion(self):
        """ Handle conversion calculation and output to label widget. """
        value = self.get_valid_miles()
        result = value * self.MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        """ increments miles by 1/-1 when up/down buttons pressed. Updates label with new conversion result. """
        value = self.get_valid_miles() + increment
        self.root.ids.input_number.text = str(value)
        self.handle_calculate_conversion()

    def get_valid_miles(self):
        """ Error handling for invalid input that is not numeric. returns '0.0' if input is not numeric. """
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0.0


ConvertMilesToKilometresApp().run()

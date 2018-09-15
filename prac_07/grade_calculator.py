"""
CP1404 prac_07.grade_calculator.py by Christopher Caferra
Kivy GUI program to calculate student grades.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class GradeCalculatorApp(App):

    def build(self):
        """Build the App from the .kv file"""
        Window.size = (400, 150)
        self.title = "Grade Calculator"
        self.root = Builder.load_file('grade_calculator.kv')
        return self.root

    def handel_calculate(self):
        """Calculate the student grade based on grade percentage"""
        value = self.get_valid_grade()
        if value < 0 or value > 100:
            result = 'Invalid percentage. Must be between 0 - 100'
        elif value < 50:
            result = 'Fail'
        elif value >= 85:
            result = 'High Distinction'
        elif 50 <= value < 65:
            result = 'Pass'
        elif 65 <= value < 75:
            result = 'Credit'
        else:
            result = "Distinction"
        self.root.ids.label_output.text = result

    def get_valid_grade(self):
        """Get a valid grade number"""
        try:
            grade = float(self.root.ids.input_number.text)
            return grade
        except ValueError:
            return 0.0


GradeCalculatorApp().run()

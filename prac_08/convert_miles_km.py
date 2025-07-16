from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

class ConvertMilesToKm(App):
    """"""
    output_text = StringProperty()
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_text = ""
        return self.root

    def handle_calculate(self, value):
        """"""
        try:
            result = float(value) * 1.60934
            self.output_text = str(result)
        except ValueError:
            self.output_text = "0.0"

    def handle_update(self):
        """Handle changes to the text input by updating the model from the view."""
        self.handle_calculate(self.root.ids.input_number.text)

    def handle_increment(self):
        try:
            value = int(self.root.ids.input_number.text)
        except ValueError:
            value = 0
        value += 1
        self.root.ids.input_number.text = str(value)
        self.handle_calculate(value)

    def handle_decrement(self):
        try:
            value = int(self.root.ids.input_number.text)
        except ValueError:
            value = 0
        value -= 1
        self.root.ids.input_number.text = str(value)
        self.handle_calculate(value)

ConvertMilesToKm().run()
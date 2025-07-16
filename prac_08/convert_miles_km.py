from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

class ConvertMilesToKm(App):
    """"""
    message = StringProperty()
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Type in the field & press Enter"
        return self.root

    def handle_calculate(self, value):
        """"""
        try:
            result = float(value) * 1.60934
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass

    def handle_update(self):
        """Handle changes to the text input by updating the model from the view."""
        self.message = self.root.ids.user_input.text

    def handle_increment(self):
        value = int(self.root.ids.input_number.text)
        value += 1
        self.root.ids.input_number.text = str(value)

    def handle_decrement(self):
        value = int(self.root.ids.input_number.text)
        value -= 1
        self.root.ids.input_number.text = str(value)

ConvertMilesToKm().run()
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KILOMETRES = 1.60934
MINIMUM_VALUE = 0
VALUE_STEP = 1

class ConvertMilesToKm(App):
    """ConvertMilesToKm is a Kivy App for converting miles to kilometres."""
    output_text = StringProperty()
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_text = ""
        return self.root

    def handle_calculate(self, value):
        """Handle calculation of miles to kilometres and update the output text."""
        try:
            result = float(value) * MILES_TO_KILOMETRES
            self.output_text = str(result)
        except ValueError:
            self.output_text = "0.0"

    def handle_update(self):
        """Recalculate kilometres when the input text is updated."""
        self.handle_calculate(self.root.ids.input_number.text)

    def handle_increment(self):
        """Handle increment of the input value by the step amount and update the output."""
        try:
            value = int(self.root.ids.input_number.text)
        except ValueError:
            value = MINIMUM_VALUE
        value += VALUE_STEP
        self.root.ids.input_number.text = str(value)
        self.handle_calculate(value)

    def handle_decrement(self):
        """Handle decrement of the input value by the step amount and update the output."""
        try:
            value = int(self.root.ids.input_number.text)
        except ValueError:
            value = MINIMUM_VALUE
        value -= VALUE_STEP
        self.root.ids.input_number.text = str(value)
        self.handle_calculate(value)

ConvertMilesToKm().run()
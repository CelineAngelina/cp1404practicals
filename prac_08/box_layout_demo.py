from kivy.app import App
from kivy.lang import Builder

class BoxLayoutKV(App):
   """BoxLayoutKV is a Kivy App for greeting user."""
   def build(self):
       """Build the Kivy app from the kv file."""
       self.root = Builder.load_file('box_layout_demo.kv')
       return self.root

   def handle_greet(self):
       """Handle the output label with a greeting using the user's input name."""
       self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

   def clear_greet(self):
       """Clear both text field and output label."""
       self.root.ids.input_name.text = ""
       self.root.ids.output_label.text = ""

BoxLayoutKV().run()
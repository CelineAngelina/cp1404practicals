from kivy.app import App
from kivy.lang import Builder

class BoxLayoutKV(App):
   def build(self):
       self.root = Builder.load_file('box_layout_demo.kv')
       return self.root

   def handle_greet(self):
       self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

   def clear_greet(self):
       self.root.ids.input_name.text = ""
       self.root.ids.output_label.text = ""

BoxLayoutKV().run()
from kivy.app import App
from kivy.lang import Builder

class BoxLayoutKV(App):
   def build(self):
       self.root = Builder.load_file('box_layout_demo.kv')
       return self.root

   def handle_greet(self):
       print("test")
       self.root.ids.output_label.text = "Hello "

BoxLayoutKV().run()
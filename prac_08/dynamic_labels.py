from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class NamesApp(App):
    """"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alex", "Celine", "Jonathan"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            name_label = Label(text=name)
            self.root.ids.main.add_widget(name_label)
        return self.root

NamesApp().run()
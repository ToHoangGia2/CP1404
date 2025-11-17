from kivy.app import App
from kivy.lang import Builder

class DynamicLabelApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Tin', 'Ben', 'Random', ':D']

    def build(self):
        self.title = "Dynamic Labels Demo"
        self.root = Builder.load_file("dynamic_labels.kv")
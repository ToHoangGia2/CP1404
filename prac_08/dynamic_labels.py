from kivy.app import App
from kivy.lang import Builder

class DynamicLabelApp(App):
    def __init__(self):
        super().__init__(**kwargs)
        self.names = ['Tin', 'Ben', 'Random', ':D']

    def build(self):
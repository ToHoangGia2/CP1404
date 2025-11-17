from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Tin', 'Ben', 'Random', ':D']

    def build(self):
        self.title = "Dynamic Labels Demo"
        self.root = Builder.load_file("dynamic_labels.kv")

        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelApp().run()
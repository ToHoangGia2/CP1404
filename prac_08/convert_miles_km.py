from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class CovertMilesApp(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Convert Miles and Km"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root


CovertMilesApp().run()
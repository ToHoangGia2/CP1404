from kivy.app import App
from kivy.lang import Builder

class CovertMilesApp(App):
    def build(self):
        self.title = "Convert Miles and Km"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root


CovertMilesApp().run()
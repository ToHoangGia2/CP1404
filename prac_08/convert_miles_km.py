from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class CovertMilesApp(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Convert Miles and Km"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def calculate(self,text):
        miles = float(text)
        km = miles * 1.60934
        self.output_km = str(km)

CovertMilesApp().run()
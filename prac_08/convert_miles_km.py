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
        miles = self.text_to_number(text)
        km = miles * 1.60934
        self.output_km = str(km)

    def text_to_number(self,text):
        try:
            miles = float(text)
        except ValueError:
            miles = 0.0
        return miles

    def up_and_down(self,text,change):
        miles = self.text_to_number(text) + change
        self.root.ids.input_mile.text = str(miles)


CovertMilesApp().run()
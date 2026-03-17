from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from file_management import FileManagement

# MyLayout --> 
class MyLayout(FloatLayout):
    # Object Instantiations
    previous_image = ObjectProperty(None)
    next_image = ObjectProperty(None)
    display_image = ObjectProperty(None)
    file_names = FileManagement()


    def __init__(self):
        super().__init__()
        self.display_image.source = self.file_names.get_current_image()

    def prev_img(self):
        self.file_names.set_previous_image()
        self.display_image.source = self.file_names.get_current_image()
        print(self.previous_image.text)

    def next_img(self):
        self.file_names.set_next_image()
        self.display_image.source = self.file_names.get_current_image()
        print(self.next_image.text)

# AxolApp --> 
class AxolApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    AxolApp().run()
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

# MyLayout --> 
class MyLayout(FloatLayout):
    pass


# AxolApp --> 
class AxolApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    AxolApp().run()
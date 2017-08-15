from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
#from kivy.lang import Builder

class app(App):
    def build(self):
        return FloatLayout()

if __name__ == '__main__':
    app().run()

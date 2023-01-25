from kivymd.app import MDApp
from application.application import Application

from kivy.core.window import Window
Window.size = (300, 500)


class MainApp(MDApp):

    def build(self):
        return Application().run()


if __name__ == '__main__':
    MainApp().run()

from kivy.lang import Builder
from kivy.properties import StringProperty, ColorProperty
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_file('board/slide/slide.kv')


class Slide(MDBoxLayout):

    source = StringProperty()
    text = StringProperty()

    color_box = ColorProperty()
    color_image = ColorProperty()
    color_label = ColorProperty()

from kivy.lang import Builder
from kivy.properties import NumericProperty, ColorProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.animation import Animation
from kivy.utils import get_color_from_hex

Builder.load_file('board/dot/dot.kv')


class Dot(MDBoxLayout):

    index = NumericProperty()
    md_bg_color = ColorProperty()

    def set_activity(self, pixel, color):

        Animation(md_bg_color=get_color_from_hex(color), d=0.2).start(self)
        self.size = [pixel, pixel]

        return

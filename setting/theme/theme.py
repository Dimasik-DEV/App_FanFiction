from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_file('setting/theme/theme.kv')


class Theme(MDScreen):

    def callback(self, instance):

        self.manager.transition.direction = 'right'
        self.manager.current = 'general'

        return

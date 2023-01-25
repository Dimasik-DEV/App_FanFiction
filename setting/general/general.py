from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_file('setting/general/general.kv')


class General(MDScreen):

    def callback(self, instance):

        self.manager.transition.direction = 'left'
        self.manager.current = instance

        return

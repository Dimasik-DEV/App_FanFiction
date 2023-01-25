from kivy.lang import Builder
from kivymd.uix.card import MDCard

Builder.load_file('history/card/card.kv')


class Card(MDCard):

    def open(self):
        # self.ids.box.add_widget(label)
        return

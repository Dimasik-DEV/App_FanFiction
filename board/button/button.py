from kivy.lang import Builder
from kivymd.uix.button import MDFillRoundFlatButton

Builder.load_file('board/button/button.kv')


class ButtonStart(MDFillRoundFlatButton):

    def press(self):
        print('Кнопка нажата')
        return

from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_file('board/board.kv')


class Board(MDScreen):

    def on_slide_complete(self, instance):

        for dot in self.ids.box_dots.children:

            # Индикация переключения слайдов
            if dot.index == instance.index:
                dot.set_activity('6dp', '#0ECBCD')

                # Активность кнопки
                if dot.index == 5:
                    self.ids.button.disabled = False
                else:
                    self.ids.button.disabled = True

            else:
                dot.set_activity('3dp', '#BABABA')

        return

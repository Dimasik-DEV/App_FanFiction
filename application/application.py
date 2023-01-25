# from board.board import Board
# from loading.loading import Loading
# from root.root import Root
# from history.card.card import Card
from setting.setting import Setting


class Application:

    def __init__(self):
        # self.app = Board()
        # self.app = Loading()
        # self.app = Root()
        # self.app = Card()
        self.app = Setting()


    def run(self):
        return self.app

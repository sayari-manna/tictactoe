from game.Board import Board
from game.Player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player(), Player()]
        self.result = -1
        self.win_sym = ''
        self.switch_user = 0

    def set_players(self, player1, player2):
        self.players[0].set_name(player1)
        self.players[1].set_name(player2)

    def symbol_validation(self, player1_sym,player2_sym):
        self.players[0].set_sym(player1_sym)
        self.players[1].set_sym(player2_sym)

    def __str__(self):
        s = ''
        for i in self.players:
            s += "{}\n".format(i)
        return s+str(self.board)

    def check(self):
        for i in self.board.win_pattern:
            if self.board.data_list[i[0]] == self.board.data_list[i[1]] == self.board.data_list[i[2]] \
                    and self.board.data_list[i[0]] != ' ':
                self.result = 1
                self.win_sym += self.board.data_list[i[0]]
                break

from os import name
from manage import main
from game import Game
from game import Board

class manager():

    def __init__(self):
        self.game = Game.Game()
        self.x = []
        self.o = []
        self.switch_user = 0
        self.win = -1

    def validate_names(self,player1_name,player2_name):
        if player1_name==player2_name:
            return 'failed'
        return 'success'

    def set_symbol(self,player1_sym):
        if player1_sym == "select menu":
            player1_sym = 'X'
            player2_sym = 'O'
        elif player1_sym == 'X':
            player2_sym = 'O'
        else:
            player2_sym = 'X'
        return player1_sym,player2_sym

    def set_values(self,player1_name,player1_sym,player2_name):
        player1_sym,player2_sym = self.set_symbol(player1_sym)
        self.game.set_players(player1_name, player2_name)
        self.game.symbol_validation(player1_sym,player2_sym)
        return self.game
        
    def main(self,flag):    
        current_user = self.game.players[0].name if self.switch_user % 2 == 0 else self.game.players[1].name
        current_sym = self.game.players[0].sym if current_user == self.game.players[0].name else self.game.players[1].sym
        next_user = self.game.players[1].name if current_user == self.game.players[0].name else self.game.players[0].name
        next_sym = self.game.players[0].sym if next_user == self.game.players[0].name else self.game.players[1].sym
        
        winner = None
        win_sym = None
        if current_sym=='O':
            self.o.append(flag)
        else:
            self.x.append(flag)
        board = Board.Board()
        win_check = board.win_pattern
        for i in win_check:
            if i[0] in self.x and i[1] in self.x and i[2] in self.x:
                win_sym = 'X'
                winner = self.game.players[0].name if self.game.players[0].sym == 'X' else self.game.players[1].name
                self.win = 1
                break
            if i[0] in self.o and i[1] in self.o and i[2] in self.o:
                win_sym = 'O'
                winner = self.game.players[0].name if self.game.players[0].sym == 'O' else self.game.players[1].name
                self.win = 1
                break
        if self.switch_user >= 8 and self.win != 1:
            self.win = 0
        self.switch_user += 1
        return next_user,next_sym,current_user,current_sym,self.win,winner,win_sym,self.x,self.o

    def set_win(self):
        self.win = -1
        self.switch_user = 0
        self.game = Game.Game()
        self.x = []
        self.o = []
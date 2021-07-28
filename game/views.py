from game import Game
import game
from game.Player import Player
from django.shortcuts import render
from django.http import HttpResponse
from game.Main import manager
from game import Game
# Create your views here.

MANAGER = manager()
class game_view():

    def start(requests):
        global MANAGER
        MANAGER = manager()
        return render(requests,"game\start.html")

    def check_data(requests):
        
        response = requests.GET
        print(response)
        result = MANAGER.validate_names(response['player'],response['opponent'])
        if result=='failed':
            return render(requests,"game/validate_names.html")
        else:
            game = MANAGER.set_values(response['player'],response['symbol'],response['opponent'])
            x = []
            o = []
            context = {'current_player':game.players[0].name,
                        'current_sym':game.players[0].sym,
                        'next_player':game.players[1].name,
                        'next_sym':game.players[1].sym,
                        'x':x,
                        'o':o}
            return render(requests,'game\game.html',context=context)

    def progress(requests):
        global MANAGER
        f = requests.POST
        flag = -1
        for i in list(f.keys()):
            if i != 'csrfmiddlewaretoken':
                flag = int(i)
        print(flag)
        current_user,current_sym,next_user,next_sym,win,winner,win_sym,x,o= MANAGER.main(flag)
        print(x)
        print(o)
        if win == -1:
            context = {'current_player':current_user,
                        'current_sym':current_sym,
                        'next_player':next_user,
                        'next_sym':next_sym,
                        'x':x,
                        'o':o}
            return render(requests,'game\game.html',context=context)
        elif win == 1:
            context = {'x':x,
                        'o':o,
                        'winner':winner,
                        'win_sym':win_sym}
            MANAGER = manager()
            return render(requests,'game/win.html',context)
        else:
            MANAGER = manager()
            context = {'current_player':current_user,
                        'current_sym':current_sym,
                        'next_player':next_user,
                        'next_sym':next_sym,
                        'x':x,
                        'o':o}
            return render(requests,'game/draw.html',context)

from game.views import game_view
from django.urls import path

urlpatterns = [
    path('start', game_view.start),
    path('validating_name',game_view.check_data),
    path('progress_game',game_view.progress)
]
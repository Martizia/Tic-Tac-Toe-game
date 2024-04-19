from player_vs_player import two_players
from player_vs_AI import player_AI

playing = True

while playing:
    game_mode = input(
        "Please select a game mode:\n1. Human vs. Human\n2. Human vs. Computer\n Press any other key to quit\n")
    match game_mode:
        case '1':
            two_players()
        case '2':
            player_AI()
        case _:
            playing = False

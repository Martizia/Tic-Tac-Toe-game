import random

def draw_board(spots):
    board = (f" {spots[1]} | {spots[2]} | {spots[3]} \n"
             f" {spots[4]} | {spots[5]} | {spots[6]} \n"
             f" {spots[7]} | {spots[8]} | {spots[9]} ")
    print(board)


def check_turn(turn):
    if turn % 2 == 0:
        return "O"
    else:
        return "X"


def check_winner(spots, p_turn):
    if (spots[1] == spots[2] == spots[3] == p_turn or
            spots[4] == spots[5] == spots[6] == p_turn or
            spots[7] == spots[8] == spots[9] == p_turn or
            spots[1] == spots[4] == spots[7] == p_turn or
            spots[2] == spots[5] == spots[8] == p_turn or
            spots[3] == spots[6] == spots[9] == p_turn or
            spots[1] == spots[5] == spots[9] == p_turn or
            spots[3] == spots[5] == spots[7] == p_turn):
        return True
    else:
        return False


def random_ai_choice(player_choices, ai_choices):
    select_choice = True
    while select_choice:
        choice = random.randint(1, 9)
        if choice not in player_choices and choice not in ai_choices:
            return choice
        select_choice = False


from helpers import draw_board, check_turn, check_winner, random_ai_choice
import os


example_spots = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
spots = {1: "_", 2: "_", 3: "_", 4: "_", 5: "_", 6: "_", 7: "_", 8: "_", 9: "_"}

player_choices = list()
ai_choices = list()


def player_AI():
    ai_playing = True
    complete = False
    turn = 0
    prev_turn = -1
    player = input("Player, please enter your name: ")
    while ai_playing:
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_board(example_spots)
        print("Use board from above to choose cell number in which you want to place your mark")
        draw_board(spots)
        # If an invalid turn has been made, let the player know
        if prev_turn == turn:
            print("Invalid Move. Please try again.")
        prev_turn = turn
        # Check if it is player 1's turn
        if (turn % 2 + 1) == 1:
            player = player
            print("Player " + player + "'s turn: Please enter a number from 1 to 9 or 'q' to quit")
            print(f"You are using '{check_turn(turn % 2 + 1)}' mark")
            # Get player input
            choice = input()
            if choice == 'q':
                ai_playing = False
            # Check if the player gave a number from 1 to 9
            elif str.isdigit(choice) and int(choice) in example_spots:
                # Check if the spot is empty
                if not spots[int(choice)] in {"X", "O"}:
                    # Update the board if valid input
                    turn += 1
                    player_choices.append(int(choice))
                    spots[int(choice)] = check_turn(turn)
        else:
            player = 'AI'
            print("AI's turn: Please wait")
            # Get AI input
            ai_choice = random_ai_choice(player_choices, ai_choices)
            # Check if the spot is empty
            if spots[ai_choice] in {"X", "O"}:
                ai_choice = random_ai_choice(player_choices, ai_choices)
                # Update the board if valid input
                turn += 1
                ai_choices.append(ai_choice)
                spots[ai_choice] = check_turn(turn)
        # Check if the game is ended and someone has won
        if check_winner(spots, check_turn(turn)):
            complete = True
            ai_playing = False
        if turn == 9 and not complete:
            ai_playing = False
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    if complete:
        if check_turn(turn) == "X":
            print(f"{player} wins!")
        else:
            print(f"AI wins!")
    else:
        print("It's a tie!")
    print("Thanks for playing!")


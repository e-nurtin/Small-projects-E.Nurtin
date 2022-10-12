import random


def print_board(board):
    print(" | ", game_board[0], " | ", game_board[1], " | ", game_board[2], " | ")
    print(" ------------------- ")
    print(" | ", game_board[3], " | ", game_board[4], " | ", game_board[5], " | ")
    print(" ------------------- ")
    print(" | ", game_board[6], " | ", game_board[7], " | ", game_board[8], " | ")


def get_marks():
    players_mark = input("Please choose 'X' or 'O':\n")
    if players_mark.lower() == "x":
        players_mark = "X"
        computers_mark = "O"
        return players_mark, computers_mark
    elif players_mark.lower() == "o":
        players_mark = "O"
        computers_mark = "X"
        return players_mark, computers_mark
    else:
        print("Please choose a valid mark!")
    return get_marks()


def get_input(player, computer):
    while True:
        player_input = input("Choose a number between 1-9:\n")
        if player_input.isdigit():
            player_choice = int(player_input) - 1
            if player_choice in available_choices:
                break
    game_board[player_choice] = player
    available_choices.remove(player_choice)
    if len(available_choices) > 0:
        computers_choice = random.choice(available_choices)
        game_board[computers_choice] = computer
        available_choices.remove(computers_choice)
        print_board(game_board)


def check_for_winner(players_mark, computers_mark, win):
    if "-" not in game_board:
        win = "tie"
    for combination in winning_combinations:
        player_count = 0
        computer_count = 0
        for index in combination:
            if game_board[index] == players_mark:
                player_count += 1
                if player_count == 3:
                    win = 'player'
            elif game_board[index] == computers_mark:
                computer_count += 1
                if computer_count == 3:
                    win = 'computer'

    return win


winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                        [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]
command = input("Press enter to start playing!\n")
players, computers = get_marks()
computer_score = 0
player_score = 0
while command != "`":
    winner = "no"
    available_choices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    game_board = ['-', '-', '-',
                  '-', '-', '-',
                  '-', '-', '-']
    print_board(game_board)
    while winner == "no":
        get_input(players, computers)
        winner = check_for_winner(players, computers, winner)
        if winner == "player":
            print("\nPlayer wins!")
            player_score += 1
            print_board(game_board)
        elif winner == "computer":
            print("\nComputer wins!")
            computer_score += 1
            print_board(game_board)
        elif winner == "tie":
            print("\nTie!")
            print_board(game_board)
    print(f"Scores:\nComputer:{computer_score}\nPlayer:{player_score}")
    command = input("\nPress enter to start playing again or '`' to exit!\n")

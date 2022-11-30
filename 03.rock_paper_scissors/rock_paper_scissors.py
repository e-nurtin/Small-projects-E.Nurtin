import random

available_choices = ["rock", "paper", "scissors"]


def get_players():
    player_two = random.choice(available_choices)
    player_one = input("Please choose one of the following:"
                       f"\n- rock = 1\n- paper = 2\n- scissors = 3\nYour "
                       f"Choice : ")
    return player_one, player_two


def game_on(player_data):
    player_one, player_two = player_data

    if player_one == "1":
        player_one = "rock"
    elif player_one == "2":
        player_one = "paper"
    elif player_one == "3":
        player_one = "scissors"
    if check_input_validity(player_one, player_two) \
            and not check_for_tie(player_one, player_two):
        check_for_winner(player_one, player_two)


def check_for_tie(player_one, player_two):
    if player_one == player_two:
        print("Draw!\nPlease choose again to continue playing!")
        game_on(get_players())
        return True
    return False


def check_for_winner(player_one, player_two):
    if player_one == "rock" and player_two == "scissors":
        winner = "player"
    elif player_one == "paper" and player_two == "rock":
        winner = "player"
    elif player_one == "scissors" and player_two == "paper":
        winner = "player"
    else:
        winner = "computer"
    return print(f"Winner is: {winner}!")


def check_input_validity(player_one, player_two):
    if player_one in available_choices:
        print(f"You chose {player_one} and computer chose {player_two}")
        return True
    else:
        print(f"Invalid choice!")
        game_on(get_players())


game_on(get_players())

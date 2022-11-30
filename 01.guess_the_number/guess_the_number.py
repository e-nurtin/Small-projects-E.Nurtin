import random


def level_of_game(lvl):
    computers_number = 0
    if lvl == 1:
        computers_number = random.randint(1, 100)
    elif lvl == 2:
        computers_number = random.randint(1, 200)
    elif lvl == 3:
        computers_number = random.randint(1, 300)
    elif lvl == 4:
        computers_number = random.randint(1, 500)
    elif lvl == 5:
        computers_number = random.randint(1, 999)
    return computers_number


def player_msg(number):
    player_input = ""
    if number == 1:
        player_input = input("Try to guess the number between 1-100: ")
    elif number == 2:
        player_input = input("Try to guess the number between 1-200: ")
    elif number == 3:
        player_input = input("Try to guess the number between 1-300: ")
    elif number == 4:
        player_input = input("Try to guess the number between 1-500: ")
    elif number == 5:
        player_input = input("Try to guess the number between 1-999: ")
    return player_input


dead = False
level = 1
for game in range(5):
    mistakes_allowed = 15
    tried_numbers = []
    computers_choice = level_of_game(level)
    while level <= 5:
        player_choice = player_msg(level)
        if player_choice in tried_numbers:
            print("You already tried that number!")
            continue
        else:
            tried_numbers.append(player_choice)
            if int(player_choice) > computers_choice:
                print("Too high!")
                mistakes_allowed -= 1
            elif int(player_choice) < computers_choice:
                print("Too low!")
                mistakes_allowed -= 1
            elif int(player_choice) == computers_choice:
                print(f"Congratulations! You guessed the number "
                      f"{computers_choice} correctly!")
                level += 1
                print()
                print(f"Next level: {level} ")
                break
            if mistakes_allowed == 0:
                dead = True
                break
            print(f"You have {mistakes_allowed} lives left!")
    if dead:
        print("You died!")
        break

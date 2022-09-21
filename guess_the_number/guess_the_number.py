import random

computers_number = random.randint(1, 101)
tried_numbers = []
number_is_found = False
while True:
    player_input = input("Try to guess the number between 1-100: ")
    if player_input.isdigit():
        tried_numbers.append(player_input)
    else:
        print("Please choose a number!")
        continue
    if player_input in tried_numbers:
        print("You already tried that number!")
    else:
        if int(player_input) > computers_number:
            print("Too high!")
        elif int(player_input) < computers_number:
            print("Too low!")
        elif int(player_input) == computers_number:
            print(f"Congratulations! You guessed the number {computers_number} "
                  f"correctly!")
            break

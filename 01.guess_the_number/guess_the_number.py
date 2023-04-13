import random


def level_of_game(number_range_to_guess_from):
	return random.randint(1, number_range_to_guess_from)


def get_player_input(number_range_to_guess_from):
	
	while True:
		player_input = input(f"Try to guess the number between 1-{number_range_to_guess_from}: ")
		
		if not player_input.isdigit() or not (1 <= int(player_input) <= number_range_to_guess_from):
			print("Please enter a valid input!")
			continue
		break
		
	return int(player_input)


dead = False

for level in range(1, 6):
	lives_left = 15
	range_to_guess_from = int(100 * (level + 0.5))
	guessed_numbers = []
	number_to_guess = level_of_game(range_to_guess_from)
	while True:
		player_choice = get_player_input(range_to_guess_from)
		
		if player_choice in guessed_numbers:
			print("You already tried that number!")
			continue
			
		else:
			guessed_numbers.append(player_choice)
			
			if int(player_choice) > number_to_guess:
				print("Too high!")
				lives_left -= 1
				
			elif int(player_choice) < number_to_guess:
				print("Too low!")
				lives_left -= 1
				
			elif int(player_choice) == number_to_guess:
				print(f"Congratulations! You guessed the number "
				      f"{number_to_guess} correctly!")
				
				print(f'Lives left: {lives_left} + 3 bonus lives = {lives_left + 3}')
				lives_left += 3
				print()
				print(f"Next level: {level + 1} ")
				break
				
			if lives_left == 0:
				dead = True
				break
			print(f"You have {lives_left} lives left!")
			
	if dead:
		print("You lose!")
		break

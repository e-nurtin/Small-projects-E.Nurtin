import random

mistake_counter = 0


def hangman_pics(counter):
    pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",

            "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

            "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

            "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",

            "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

            "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

            "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]
    return print(pics[counter])


def ask_for_input():
    user_input = input("Guess a letter or word: ").upper()
    return user_input


def letter_not_in_word(guessed_letter, counter, original_word):
    counter += 1
    if counter == 6:
        hangman_pics(counter)
        print("Game over! You lost!")
        print(f"Original word: {original_word}")
        game_on()
    print(f"'{guessed_letter}' is not in the word! You have "
          f"{6 - counter} attempts left before getting "
          f"hanged!")
    return counter


def check_guessed_letter(letter, list_of_letters, word, guess_word):
    if letter.isalpha():
        if letter in list_of_letters:
            print("You already guessed that letter!")
            check_guessed_letter(ask_for_input(), list_of_letters, word, guess_word)
        else:
            list_of_letters.append(letter)
            if letter in word and letter not in guess_word:
                return True
    return False


def main_game(word, original, counter):
    guess_word = list(len(word) * "_")
    msg = f"Current word length: {len(word)}"
    output = "".join(guess_word)
    guessed_letters = []
    while not output.isalpha():
        print(msg, output)
        hangman_pics(counter)
        guess_letter = ask_for_input()

        if not check_guessed_letter(guess_letter, guessed_letters,
                                    word, guess_word):
            counter = letter_not_in_word(guess_letter, counter, original)
            continue

        for index in range(len(word)):
            if word[index] == guess_letter:
                guess_word[index] = guess_letter
        word = word.replace(guess_letter, "*")
        output = "".join(guess_word)
    print("Congratulations! You win!")
    game_on()


def check_game(word):
    if word == "2":
        words = (
            'ant baboon badger bat bear beaver camel cat clam cobra cougar '
            'coyote crow deer dog donkey duck eagle ferret fox frog goat '
            'goose hawk lion lizard llama mole monkey moose mouse mule newt '
            'otter owl panda parrot pigeon python rabbit ram rat raven '
            'rhino salmon seal shark sheep skunk sloth snake spider '
            'stork swan tiger toad trout turkey turtle weasel whale wolf '
            'combat zebra ').split()
        word = random.choice(words).upper()
    if word.isalpha():
        return word
    else:
        game_on()


def game_on():
    initial_word = input("\nPlease choose a valid word to start playing with "
                         "another player or type '2' to play against the "
                         "computer:\n\n-").upper()
    initial_word = check_game(initial_word)
    original_word = initial_word
    main_game(initial_word, original_word, mistake_counter)


game_on()

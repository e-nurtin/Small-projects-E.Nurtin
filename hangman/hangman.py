import random


def hangman_pics(counter):
    pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",

            "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

            "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

            "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",

            "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

            "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

            "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]
    return print(pics[counter[0]])


def letter_not_in_word(guessed, count, output, original):
    count[0] += 1
    if count[0] == 6:
        hangman_pics(count)
        print("Game is over! You lost!")
        print(f"Original word: {original}")
        exit()
    print(output)
    hangman_pics(count)
    print(f"'{guessed}' is not in the word! You have "
          f"{6 - count[0]} attempts left before getting "
          f"hanged!")


def check_guessed_letter(letter, list_of_letters, word, guess_word,
                         count_of_mistakes, output, original):
    if letter.isalpha():
        if letter not in list_of_letters:
            list_of_letters.append(letter)
            if letter in word and letter not in guess_word:
                return True
            else:
                letter_not_in_word(letter, count_of_mistakes, output, original)
        else:
            return False


def main_game(word, original):
    guess_word = list(len(word) * "_")
    msg = f"Current word length: {len(word)}"
    output = "".join(guess_word)
    guessed_letters = []
    mistake_counter = [0]
    while not output.isalpha():
        print(msg, "\n", output)
        hangman_pics(mistake_counter)
        guess_letter = input("Guess a letter or word: ").upper()

        while not check_guessed_letter(guess_letter, guessed_letters,
                         word, guess_word, mistake_counter, output, original):
            guess_letter = input("Guess a letter or word: ").upper()

        for index in range(len(word)):
            if word[index] == guess_letter:
                guess_word[index] = guess_letter
        word = word.replace(guess_letter, "*")
        output = "".join(guess_word)
    return print("Congratulations! You win!")


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
    main_game(initial_word, original_word)


game_on()

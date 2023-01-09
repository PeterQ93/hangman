from words import word_list
import random


def get_word():
    """
    Fetches random word from words.py and returns it in capital letters
    """
    random_word = random.choice(word_list)
    return random_word.upper()


def homepage():
    """
    Homepage the user is first brought to.
    Gives them the option to start the game or to read the rules.
    """
    word = get_word()
    homepage_graphic()
    print(display_hangman(0))
    print('Type 1 to begin game\n')
    print('Type 2 to read the instructions')
    selection = False
    while not selection:
        choice = input(' \n')
        if choice == '1':
            selection = True
            start_game(word)
        elif choice == '2':
            selection = True
            rules()
        else:
            print('\n Please type 1 or 2 to make your choice.')


def rules():
    """
    Display instructions for play the game.
    """
    print('1. Try to guess the word by typing 1 letter at a time.')
    print('2. Every wrong answer will cost you one life.')
    print('3. The Hanging will begin once a life is lost')
    print('4. Once you run out of lives its gameover')
    print('5. Win the game by guessing the correct letters')
    print('6. Good Luck you will need it!')
         

    start = input('Press the enter key to return to the Homepage.\n')
    homepage()


def start_game(word):
    """
    Starts the game and hides the word for the player.
    It checks if the letter input is correct,
    if not it prompts user for input, then checks if it's in the word.
    Iterates through hidden word and substitutes letters where appropriate.
    Checks if the game is finished and displays the relative message.
    Displays stats like chances left, visual rep of chances left, which letters
    have been used and the hidden word or correct letters.
    """
    game_word = '_' * len(word)
    endgame = False
    guessed_letters = []
    chances = 6
    print(display_hangman(chances))
    print('Save the fellow from the gallows!\n')
    print(f'Chances left: {chances}\n')
    print('Guess this word: ' + ''.join(game_word) + '\n')
    while not endgame and chances > 0:
        guess = input('Try a letter:\n').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f'You have already tried {guess}!')
            elif guess not in word:
                print(f'Woops {guess} is not what we are looking for!')
                chances -= 1
                guessed_letters.append(guess)
            else:
                print(f'Great {guess} is in the word well done!')
                guessed_letters.append(guess)
                word_as_list = list(game_word)
                indices = [
                    i for i, letter in enumerate(word)
                    if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                game_word = ''.join(word_as_list)
                if '_' not in game_word:
                    endgame = True
        elif len(guess) != 1:
            print('Oh no, you have to guess one letter at a time!')
            print(f'You used {len(guess)} characters.\n')
        else:
            print('Sorry you can only guess letters!')
            print(f'{guess} is not a letter!')
        print(display_hangman(chances))
        print(f'Chances left: {chances}\n')
        print('Guess this word: ' + ', '.join(game_word) + '\n')
        print('Letters tried: ' + ', '.join(guessed_letters) + '\n')
    if endgame:
        display_win()
        print('Nice one you got it right!')
    else:
        display_lose()
        print('To the gallows you go better luck next time!')
        print(f'The word was: {word}.')
    restart_game()


def restart_game():
    

        







    


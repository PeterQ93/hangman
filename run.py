"""
Hangman Game created by Peter Quigley
"""
import random
from words import word_list
from classes.graphics import homepage_graphic, display_win, display_lose,\
     display_hangman, Color


def get_word():
    """
    Fetches random word from words.py and returns it in capital letters
    """
    random_word = random.choice(word_list)
    return random_word.upper()


def welcome():
    """
    Homepage the user is first brought to.
    Gives them the option to start the game or to read the rules.
    """
    word = get_word()
    homepage_graphic()
    print(display_hangman(0))
    print(f'{Color.GREEN}Type 1 to begin game{Color.RESET}\n')
    print(f'{Color.YELLOW}Type 2 to read the rules{Color.RESET}')
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
    print('1. Choose your difficulty.')
    print('2. Try to guess the word by typing 1 letter at a time.')
    print('3. Every wrong answer will cost you one life.')
    print('4. The Hanging will begin once a life is lost')
    print('5. Once you run out of lives its gameover')
    print('6. Win the game by guessing the correct letters')
    print('7. Good Luck you will need it!')
    input('Press the enter key to return to the Homepage.\n')
    welcome()


def start_game(word):
    """
    Displays word for each turn, will run until
    user guesses word or runs out of tries.
    """
    game_word = '_' * len(word)
    endgame = False
    guessed_letters = []
    chances = set_difficulty()
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
                positions = [
                    i for i, letter in enumerate(word)
                    if letter == guess]
                for index in positions:
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
    else:
        display_lose(word)
    restart_game()


def set_difficulty():
    """
    Sets difficulty for game
    """
    lives = 0
    difficulty_selected = False
    while difficulty_selected is False:
        difficulty = input("""Please select difficulty:
E = Easy, M = Medium, H = Hard: """).upper()
        if difficulty == 'E':
            lives = 8
            print('You chose Easy difficulty. You have ', lives, 'chances')
            difficulty_selected = True
        elif difficulty == 'M':
            lives = 6
            print('You chose Medium difficulty. You have ', lives, 'chances')
            difficulty_selected = True
        elif difficulty == 'H':
            lives = 4
            print('You chose Hard difficulty. You have ', lives, 'chances')
            difficulty_selected = True
        else:
            print(difficulty, 'is not a difficulty')
    return lives


def restart_game():
    """
    Asks if the player wants to restard the game.
    If not, returns to homepage.
    """
    restart_option = input('Would you like to play again? Y or N\n').upper()
    if restart_option == 'Y':
        word = get_word()
        start_game(word)
    elif restart_option == 'N':
        welcome()
    else:
        print('Pick Y or N!')
        print(f'You picked {restart_option}')
        restart_game()


welcome()

import random
from words import word_list


class Color:
    """
    Colors to be called for text within this file
    """
    RESET = '\033[0m'
    BLUE = '\u001b[34m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\u001b[33m'


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
    print('1. Try to guess the word by typing 1 letter at a time.')
    print('2. Every wrong answer will cost you one life.')
    print('3. The Hanging will begin once a life is lost')
    print('4. Once you run out of lives its gameover')
    print('5. Win the game by guessing the correct letters')
    print('6. Good Luck you will need it!')
    input('Press the enter key to return to the Homepage.\n')
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
    difficulty_selected = False
    while difficulty_selected is False:
        difficulty = input("""Please select difficulty:
E = Easy, M = Medium, H = Hard: """).upper()
        if difficulty == 'E':
            chances = 6
            print('You chose Easy difficulty. You have ', chances, 'chances')
            difficulty_selected = True
        elif difficulty == 'M':
            chances = 4
            print('You chose Medium difficulty. You have ', chances, 'chances')
            difficulty_selected = True
        elif difficulty == 'H':
            chances = 3
            print('You chose Hard difficulty. You have ', chances, 'chances')
            difficulty_selected = True
        else:
            print(difficulty, 'is not a difficulty')
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
    """
    Asks if the player wants to restard the game.
    If not, returns to homepage.
    """
    restart_option = input('Would you like to play again?').upper()
    if restart_option == 'Y':
        word = get_word()
        start_game(word)
    elif restart_option == 'N':
        homepage()
    else:
        print('Pick Y or N!')
        print(f'You picked {restart_option}')
        restart_game()


def display_hangman(chances):
    """
    The gradual progression of the hangman game.
    """
    hanging_man = [  # final state: head, torso, both arms, and both legs
                f"""{Color.BLUE}
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                {Color.RESET}""",
                # head, torso, both arms, and one leg
                f"""{Color.BLUE}
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                {Color.RESET}""",
                # head, torso, and both arms
                f"""{Color.BLUE}
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                {Color.RESET}""",
                # head, torso, and one arm
                f"""{Color.BLUE}
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                {Color.RESET}""",
                # head and torso
                f"""{Color.BLUE}
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                {Color.RESET}""",
                # head
                f"""{Color.BLUE}
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                {Color.RESET}""",
                # initial empty state
                f"""{Color.BLUE}
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                {Color.RESET}"""
    ]
    return hanging_man[chances]


def homepage_graphic():
    """
    Graphic to be diplayed on Homepage
    """
    print(f"""{Color.BLUE}  
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/  {Color.RESET}""")


def display_win():
    """
    Display a graphic for if the player wins the game
    """
    print(f"""You guessed the word! You Win! {Color.GREEN}

██     ██ ███████ ██      ██
██     ██ ██      ██      ██
██  █  ██ █████   ██      ██
██ ███ ██ ██      ██      ██
 ███ ███  ███████ ███████ ███████
██████   ██████  ███    ██ ███████ ██
██   ██ ██    ██ ████   ██ ██      ██
██   ██ ██    ██ ██ ██  ██ █████   ██
██   ██ ██    ██ ██  ██ ██ ██
██████   ██████  ██   ████ ███████ ██
    
    {Color.RESET}""")


def display_lose():
    """
    Display a graphic for if the player loses the game.
    """
    print(f"""{Color.RED}
                    --------
                    |      |
                    |      O
                    |     \|/
                    |      |
                    |     / \.
                    -
    ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
   ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
  ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
  ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
  ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
   ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
   ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
   ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░
    ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░
                                                      ░
    {Color.RESET}""")  


homepage()

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



    


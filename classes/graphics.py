"""
Graphics page to keep python code tidy.
"""


class Color:
    """
    Colors to be called for text within this file
    """
    RESET = '\033[0m'
    BLUE = '\u001b[34m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\u001b[33m'


def homepage_graphic():
    """
    Graphic to be diplayed on Homepage
    """
    print(f"""{Color.BLUE}
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
 {Color.RESET}""")


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
    print('Nice one you got it right!')


def display_lose(word):
    """
    Display a graphic for if the player loses the game.
    """
    print(f"""{Color.RED}
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
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
    print('To the gallows you go better luck next time!')
    print(f'The word was: {word}.')


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
                # start of rope
                f"""{Color.BLUE}
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                {Color.RESET}""",
                # full pole
                f"""{Color.BLUE}

                   |
                   |
                   |
                   |
                   |
                   -
                {Color.RESET}""",
                # half pole
                f"""{Color.BLUE}
                   |
                   |
                   -
                {Color.RESET}"""
    ]
    return hanging_man[chances]

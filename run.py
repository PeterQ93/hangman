from words import word_list
import random



def get_word():
    """
    Fetches random word from words.py and returns it in capital letters
    """
    word = random.choice(word_list)
    return word.upper()
    

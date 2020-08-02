import json
from difflib import get_close_matches
import dictDB

def translate(word):
    results = dictDB.get_definitions(word.lower())
    
    if not results:
        results = dictDB.get_definitions(word.upper())
 
    if not results:
        results = dictDB.get_definitions(word.title)

    if not results:
        all_words = dictDB.get_all_words()
        close_matches = get_close_matches(word, all_words)
        if close_matches:
            closest_word = close_matches[0]
            if confirm_word(closest_word):
                results = dictDB.get_definitions(closest_word)
    
    if not results:
        results = "The word does not exist. Please check it."
    
    return results 

def confirm_word(word):
    message = "Did you mean \"{}\" instead? Enter \"Y\" if yes, or \"N\" if no. ".format(word)
    confirm = input(message).upper()
    return confirm == "Y"

def print_output(output):
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)


if __name__ == "__main__":
    word = input("Enter word: ")
    output = translate(word)
    print_output(output)
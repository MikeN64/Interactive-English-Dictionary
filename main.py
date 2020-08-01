import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word.lower() in data:
        return data[word.lower()]

    if word.upper() in data:
        return data[word.upper()]

    if word.title() in data:
        return data[word.title()]
        
    close_matches = get_close_matches(word, data.keys())
    if close_matches:
        closest_word = close_matches[0]
        if confirm_word(closest_word):
            return data[closest_word]
        
    return "The word does not exist. Please check it."

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
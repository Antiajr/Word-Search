import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    Word = word.lower()
    if Word in data:
        return data[Word]
    elif len(get_close_matches(word, data.keys()))>0:
        yn = input("did you mean %s instead ? Enter Y if yes, or N if no: " % get_close_matches(Word, data.keys())[0])
        yn = yn.upper()
        if yn == "Y":
            return data[get_close_matches(Word, data.keys())[0]]

        elif yn == "N":
            return "The Word dosen't exist. Please double check it"
        else:
            return "Invalid input..."
    else:
        return "Word not found.Please double check it."

word = input("Enter Word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

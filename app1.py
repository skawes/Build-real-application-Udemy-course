import json
from difflib import get_close_matches as matcher

data = json.load(open("E:\\data.json"))


def translate(word):
    if word.lower() in data:
        return data[word.lower()]
    else:
        close_word = matcher(word, data.keys(), 1)
        option = input("Did you mean  {} :".format(close_word[0]))
        if option == 'yes':
            word = close_word[0]
            return data[word.lower()]
        else:
            return "The word doesnt exist please check again!"


word = input('Enter a word: ')
output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)

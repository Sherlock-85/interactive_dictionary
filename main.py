import json
from difflib import get_close_matches

dict_data = json.load(open("data.json"))

def dictionary(k):
    k = k.lower()
    if k in dict_data:
        return dict_data[k]
    elif k.title() in dict_data:
        return dict_data[k.title()]
    elif k.upper() in dict_data:
        return dict_data[k.upper()]
    elif k in dict_data:
        return dict_data[k]
    elif k not in dict_data:
        matches = get_close_matches(k, dict_data.keys(), cutoff=0.8)
        if matches:
            best_match = matches[0]
            correct_match = input(f"Did you mean {best_match}? Enter Y if yes or N if no: ")
            if correct_match.upper() == 'Y':
                return dict_data[best_match]
            elif correct_match.upper() == 'N':
                return 'The entry is not found in the dictionary. Please try a different word.'
            else:
                return 'You have entered an invalid input.'
        else:
            return 'The entry is not found in the dictionary. Please try a different word.'


key = input("Enter a word you would like the definition to: ")

output = dictionary(key)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)





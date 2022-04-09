import pprint
from collections import defaultdict
def aplha_chart():
    string = input("Create bar garph alphabets: ")
    string = string.lower()#converting any capital letters to small case
    di = defaultdict(list)

    for character in string:
        if character.isalpha():
            di[character].append(character)
    pprint.pprint(di,width=10)
aplha_chart()




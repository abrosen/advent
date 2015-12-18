import re

data = open("12.txt", 'r').read()
pattern = r'-*\d+'


print(sum(map(int, re.findall(pattern, data))))


import json
x = json.loads(data)


def evaluate(x):
    if type(x) == int:
        return x
    if type(x) == list:
        return sum(map(evaluate, x))
    if type(x) == dict:
        if 'red' in x.values():
            return 0
        else:
            return sum(map(evaluate, x.values()))
    return 0

print(evaluate(x))

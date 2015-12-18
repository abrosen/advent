import re


test1 = "hijklmmz"
test2 = "abbceffg"
test3 = "abbegjk"

test = test1

pattern1 = r'[iol]'
pattern2 = r'(\w)\1\w*(\w)\2'


def increment(p):
    p = list(p)
    for i in range(len(p) - 1, -1, -1):
        if p[i] == 'z':
            p[i] = 'a'
        else:
            p[i] = chr(ord(p[i]) + 1)
            break
    return ''.join(p)


def nextPassword(p):
    while True:
        p = increment(p)
        match = re.search(pattern1, p)
        if match:
            continue

        match = re.search(pattern2, p)
        if not match:
            continue

        p = list(p)
        for i in range(0, len(p) - 2):
            if (ord(p[i + 1]) == (ord(p[i]) + 1)) and (ord(p[i + 2]) == (ord(p[i]) + 2)):
                return ''.join(p)
        ''.join(p)

p = "hepxcrrq"
p = nextPassword(p)
print(p)
p = nextPassword(p)
print(p)

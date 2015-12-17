def lookAndSay(num):
    num = str(num)
    output = ""
    i = 0
    instances = 1
    while i < len(num):
        if i + 1 == len(num) or num[i] != num[i + 1]:
            output += str(instances) + num[i]
            i += 1
            instances = 1
        else:
            instances += 1
            i += 1
    return output

x = 1113122113
for i in range(0, 50):
    x = lookAndSay(x)
    print(len(x))

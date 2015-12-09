
signals = {}


def evaluate(args):
    args = args.split()
    if len(args) == 1:
        if args[0].isdigit():
            return int(args[0])
        else:
            return signals[args[0]]
    elif len(args) == 2:
        if args[1].isdigit():
            return 65535 & ~int(args[1])
        else:
            return 65535 & ~signals[args[1]]
    else:
        l = int(args[0]) if args[0].isdigit() else signals[args[0]]
        r = int(args[2]) if args[2].isdigit() else signals[args[2]]
        op = args[1]
        if op == 'AND':
            return l & r
        elif op == 'OR':
            return l | r
        elif op == 'RSHIFT':
            return l >> r
        elif op == 'LSHIFT':
            return l << r % 65535


instructions = open("7.txt", 'r').readlines()
for line in instructions:
    line = line.strip()


while len(instructions):
    for line in instructions[:]:
        args, output = line.split("->")
        output = output.strip()
        try:
            signals[output] = evaluate(args)
            instructions.remove(line)
        except Exception as e:
            continue

print(signals['a'])
ans = signals['a']

instructions = open("7.txt", 'r').readlines()
for line in instructions:
    line = line.strip()

signals = {}

while len(instructions):
    for line in instructions[:]:
        args, output = line.split("->")
        output = output.strip()
        if output == 'b':
            signals['b'] = ans
            instructions.remove(line)
            continue
        try:
            signals[output] = evaluate(args)
            instructions.remove(line)
        except Exception as e:
            continue
print(signals['a'])

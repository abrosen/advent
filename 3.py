
x = 0
y = 0
rx = 0 
ry = 0

robot_turn = True

grid = {}
grid[(x,y)] = 2
data =  open("input3.txt").read()

for c  in data:
    a = ()
    if not robot_turn:
        if   c == '^':
            y += 1
        elif c =='v':
            y -= 1
        elif c == '<':
            x -= 1
        elif c == '>':
            x += 1
        a = (x,y)
        robot_turn = True
    else:
        if  c == '^':
            ry += 1
        elif c =='v':
            ry -= 1
        elif c == '<':
            rx -= 1
        elif c == '>':
            rx += 1
        robot_turn = False
        a = (rx,ry)
    
    
    if a in grid:
        grid[a] +=1
    else:
        grid[a] = 1

print(len(grid.keys()))

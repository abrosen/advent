grid= []
lines = open("18.txt").readlines()
for line in  lines:
    row = []
    line = line.strip()
    for c in line:
        if c =="#":
            row.append(1)
        elif c == ".":
            row.append(0)
    grid.append(row)


grid[0][0] = 1
grid[0][len(grid) -1] = 1
grid[len(grid) -1][0] = 1
grid[len(grid) -1][len(grid) -1] = 1

nextGrid = [ row[:] for row in grid]



def countNeighbors(grid,x,y):
    count = 0
    if x != 0 and y!=0:
        count += grid[x-1][y-1]
    if y!=0:
        count += grid[x][y-1]
    if x != len(grid)-1 and y!=0:
        count += grid[x+1][y-1]
    
    if x !=0:
        count += grid[x-1][y]
    if x != len(grid)-1:
        count += grid[x+1][y]
        
    if x != 0 and y != len(grid)-1:
        count += grid[x-1][y+1]
    if y != len(grid) - 1:
        count += grid[x][y+1]
    if x != len(grid)-1 and y != len(grid)-1:
        count += grid[x+1][y+1]
    return count

def printGrid(grid):
    
    for line in grid:
        s = ""
        for t in line:
            if t:
                s+='#'
            else:
                s+='.'
        print(s)
    print("\n")




gens = 100
printGrid(grid)
for tick in range(gens):
    for i in range(len(grid)):
        for j in range(len(grid)):
            count = countNeighbors(grid,i,j)
            if grid[i][j]:
                if count !=2 and count !=3:
                    nextGrid[i][j] = 0
            else:
                if count ==3:
                    nextGrid[i][j] =1
    
    nextGrid[0][0] = 1
    nextGrid[0][len(grid) -1] = 1
    nextGrid[len(grid) -1][0] = 1
    nextGrid[len(grid) -1][len(grid) -1] = 1
    grid =[row[:] for row in nextGrid]
    print(sum(map(sum , grid)))
    
    




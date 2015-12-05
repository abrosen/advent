

floor = 0 
position =  0 

data = open("input.txt",'r').read()
print(data)
for c in data:
    if c =='(':
        floor = floor +1
    elif c == ')':
        floor = floor -1
    position += 1
    if floor == -1:
        break
        
print(floor)    
print(position)

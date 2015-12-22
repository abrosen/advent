timeLimit = 2503

class Reindeer(object):
    def __init__(self,name,speed,limit,rest):
        self.name = name
        self.speed = speed
        self.limit = limit
        self.rest = rest
        self.moving = True 
        self.time_traveled = 0
        self.time_rested = 0
        self.distance = 0  
        self.points = 0
        
    def __str__(self):
        return self.name + ": "+ str(self.distance) + "\t\t\t" +str(self.points)

def getLeaders(racers):
    leaders = [racers[0]]
    for r in racers[1:]:
        if r.distance == leaders[0].distance:
            leaders.append(r)
        elif leaders[0].distance < r.distance :
            leaders = [r]
    return leaders


data = open("14.txt",'r').readlines()
racers =  []




for line in data:
    line = line.split()
    r = Reindeer(line[0],int(line[3]), int(line[6]), int(line[13]))
    racers.append(r)
    
for t in range(0,timeLimit):
    for r in racers:
        if r.moving:
            r.distance += r.speed
            r.time_traveled += 1
            if  r.time_traveled >= r.limit:
                r.moving = False
                r.time_traveled = 0
        else:
            r.time_rested += 1
            if r.time_rested >= r.rest:
                r.moving = True
                r.time_rested = 0
    leaders =  getLeaders(racers)
    for l in leaders:
        l.points += 1
        
for r in racers:
    print(r)

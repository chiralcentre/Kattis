from sys import stdin,stdout
from functools import cmp_to_key

class Adventurer():
    def __init__(self,name,s1,s2,s3):
        self.name = name
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

def compareS1(x,y):
    x1,y1 = x.s1,y.s1
    if x1 != y1:
        return x1 - y1
    else: # if skill level is the same, compare names and arrange in descending order
        return 1 if y.name > x.name else -1 #names are unique
    
def compareS2(x,y):
    x2,y2 = x.s2,y.s2
    if x2 != y2:
        return x2 - y2
    else: # if skill level is the same, compare names and arrange in descending order
        return 1 if y.name > x.name else -1 #names are unique

def compareS3(x,y):
    x3,y3 = x.s3,y.s3
    if x3 != y3:
        return x3 - y3
    else: # if skill level is the same, compare names and arrange in descending order
        return 1 if y.name > x.name else -1 #names are unique
    
N = int(stdin.readline())
firstSkill,secondSkill,thirdSkill,teams = [],[],[],[]
for _ in range(N):
    name,s1,s2,s3 = stdin.readline().split()
    firstSkill.append(Adventurer(name,int(s1),int(s2),int(s3)))
    secondSkill.append(Adventurer(name,int(s1),int(s2),int(s3)))
    thirdSkill.append(Adventurer(name,int(s1),int(s2),int(s3)))
# sort by skill rating in ascending order and name in descending lexicographical order
firstSkill.sort(key = cmp_to_key(compareS1))
secondSkill.sort(key = cmp_to_key(compareS2))
thirdSkill.sort(key = cmp_to_key(compareS3))
deleted = set()
while N >= 3:
    team = []
    while firstSkill and firstSkill[-1].name in deleted:
        firstSkill.pop()
    firstPlayer = firstSkill.pop()
    deleted.add(firstPlayer.name)
    team.append(firstPlayer.name)
    while secondSkill and secondSkill[-1].name in deleted:
        secondSkill.pop()
    secondPlayer = secondSkill.pop()
    deleted.add(secondPlayer.name)
    team.append(secondPlayer.name)
    while thirdSkill and thirdSkill[-1].name in deleted:
        thirdSkill.pop()
    thirdPlayer = thirdSkill.pop()
    deleted.add(thirdPlayer.name)
    team.append(thirdPlayer.name)
    N -= 3
    teams.append(sorted(team))

for team in teams:
    stdout.write(' '.join(team)+'\n')

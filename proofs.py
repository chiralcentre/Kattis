from sys import stdin,stdout

def proof():
    conclusions = set()
    for i in range(int(stdin.readline())):
        a,c = stdin.readline().split("-> ")
        assumptions = a.strip().split()
        for statement in assumptions:
            if statement not in conclusions:
                return str(i+1)
        conclusions.add(c.strip()) #remove \n character
    return "correct"

stdout.write(proof())
        

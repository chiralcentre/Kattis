from sys import stdin,stdout

n,k = map(int,stdin.readline().split())
commands = stdin.readline().split()
egg_positions = [0] #start from position 0
for i in range(len(commands)):
    if commands[i] == "undo":
        for j in range(int(commands[i+1])):
            egg_positions.pop()
    elif i == 0 or commands[i-1] != "undo":
        egg_positions.append((egg_positions[-1] + int(commands[i]))%n)
stdout.write(str(egg_positions[-1]))
            

import sys

problems,solved = {},{}

for line in sys.stdin:
    entry = line.split()
    if int(entry[0]) == -1:
        break
    if entry[1] not in problems:
        problems[entry[1]] = 1
    else:
        problems[entry[1]] += 1
    if entry[2] == 'right':
        solved[entry[1]] = int(entry[0])
        
counter = 0
for key in solved:
    attempts = problems[key]
    counter += solved[key] + (attempts - 1)*20
print(f'{len(solved)} {counter}')
    
    

import sys

dict1 = {}

for line in sys.stdin:
    if len(line.strip()) == 0:
        break
    inpt = list(line.split())
    dict1[inpt[1]] = inpt[0]
    
for line in sys.stdin:
    word = line.strip()
    if len(word) == 0:
        break
    print(dict1[word]) if word in dict1.keys() else print('eh')
    

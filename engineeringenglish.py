import sys

dict1 = {}

for line in sys.stdin:
    inpt = line.split()
    lst = []
    for word in inpt:
        if word.lower() not in dict1.keys():
            dict1[word.lower()] = 1
            lst.append(word)
        else:
            lst.append('.')
    print(' '.join(lst))

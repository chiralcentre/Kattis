from collections import deque
from functools import cmp_to_key

def compare(x,y):
    classes = {'upper':2,'middle':1,'lower':0}
    social_class1,social_class2 = x[1],y[1]
    for i in range(len(y[1])-1,-1,-1):
        rank = classes[social_class2[i]] - classes[social_class1[i]]
        if rank != 0:
            return rank
    # if all levels of detail are the same, compare names
    return 1 if x[0] > y[0] else -1 #names are all different

for i in range(int(input())):
    persons,max_length = [],0
    for j in range(int(input())):
        line = input().split()
        name,social_class = line[0][:-1],deque(line[1].split("-"))
        if len(social_class) > max_length:
            max_length = len(social_class)
        persons.append([name,social_class])
    for p in persons:
        for k in range(max_length - len(p[1])):
            p[1].appendleft("middle") #leading middles
    persons = sorted(persons,key = cmp_to_key(compare))
    for x,y in persons:
        print(x)
    print("="*30)

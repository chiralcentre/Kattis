def recurrence_index(prev):
    counter = 2
    while True:
        current = len(str(prev))
        if current == prev:
            return counter
        else:
            counter += 1
            prev = current
    

while True:
    initial = input().strip()
    if initial == 'END':
        break
    l = len(initial)
    if l == 1 and int(initial) == 1:
        print(1)
    else:
        print(recurrence_index(l))

'''
#time limit exceeded
def recurrence_index(prev):
    counter = 1
    while True:
        current = len(str(prev))
        if current == prev:
            return counter
        else:
            counter += 1
            prev = current
    

while True:
    initial = input().strip()
    if initial == 'END':
        break
    initial = int(initial)
    print(recurrence_index(initial))
'''

'''
# time limit exceeded
from math import floor,log10
def recurrence_index(prev):
    return floor(log10(prev)) + 2 if prev > 0 else 2

while True:
    initial = input().strip()
    if initial == 'END':
        break
    initial = int(initial)
    print(recurrence_index(initial))
'''

'''
#time limit exceeded
from math import floor,log10

def digits(n):
    return floor(log10(n)+1) if n > 0 else 1 # assuming n >= 0

while True:
    initial = input().strip()
    if initial == 'END':
        break
    initial = int(initial)
    counter,current = 1,digits(initial)
    while current != initial:
        initial = current
        current = digits(current)
        #print(f'initial = {initial},current = {current}')
        counter += 1 
    print(counter)
'''

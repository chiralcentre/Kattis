upper_left,lower_left,upper_right,lower_right = {f'+{i}' for i in range(8,0,-1)},{f'-{i}' for i in range(8,0,-1)},{f'{i}+' for i in range(8,0,-1)},{f'{i}-' for i in range(8,0,-1)}
#The built-in method, discard() in Python, removes the element from the set only if the element is present in the set. If the element is not present in the set, then no error or exception is raised and the original set is printed
for _ in range(int(input())):
    tooth,problem = input().split()
    if problem == 'm':
        if tooth[0] == '+':
            upper_left.discard(tooth)
        elif tooth[1] == '+':
            upper_right.discard(tooth)
        elif tooth[0] == '-':
            lower_left.discard(tooth)
        elif tooth[1] == '-':
            lower_right.discard(tooth)
    else: #bluetooth
        if tooth[0] == '+':
            upper_left.clear()
        elif tooth[1] == '+':
            upper_right.clear()
        elif tooth[0] == '-':
            lower_left.clear()
        elif tooth[1] == '-':
            lower_right.clear()

print('0') if len(upper_left) > 0 and len(lower_left) > 0 else print('1') if len(upper_right) > 0 and len(lower_right) > 0 else print('2')


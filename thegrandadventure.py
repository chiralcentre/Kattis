from sys import stdin,stdout

def completeAdventure(adventure):
    stack = []
    for char in adventure:
        if char != '.':
            if char not in villains: #item
                stack.append(char)
            else:
                if stack and villains[char] == stack[-1]:
                    stack.pop()
                else:
                    return "NO"
    return "YES" if not stack else "NO"
                
villains = {'b':'$','t':'|','j':'*'}
for _ in range(int(stdin.readline())):
    adventure = stdin.readline().strip()
    stdout.write(completeAdventure(adventure)+'\n')

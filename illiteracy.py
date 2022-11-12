from collections import deque

rotations = {"A": "B", "B": "C", "C": "D",
             "D": "E", "E": "F", "F": "A"}

def A(i, s):
    return f'{(s[:i-1] + rotations[s[i-1]] if i > 0 else "")}A{(rotations[s[i+1]] + s[i+2:] if i < len(s) - 1 else "")}'

def B(i, string):
    if i in range(1,len(string)-1):
        return string[:i+1] + string[i-1] + string[i+2:]
    return string

def C(i, string):
    return string[:7-i] + rotations[string[7-i]] + string[8-i:]

def D(i, string):
    if i in range(1,len(string)-1):
        if i < (len(string)//2):
            return ''.join(rotations[string[j]] for j in range(i)) + string[i:]
        else:
            return string[:i+1] + ''.join(rotations[string[j]] for j in range(i+1,len(string)))
    return string

def E(i, string):
    if i in range(1,len(string)-1):
        y = min(i,len(string) - 1 - i)
        a = rotations[string[i - y]]
        b = rotations[string[i + y]]
        return string[:i-y] + a + string[i-y+1:i+y] + b + string[i+y+1:]
    return string

def F(i, string):
    i += 1
    rotationIndex = (i + 9) // 2 if i % 2 else i // 2
    rotationIndex -= 1  
    return string[:rotationIndex] + rotations[string[rotationIndex]] + string[rotationIndex+1:]

def click(index,string):
    effects = {"A": A, "B": B, "C": C,
               "D": D, "E": E, "F": F}
    return effects[string[index]](index,string)


def solve(start,target):
    if start == target:
        return "0"
    frontier = deque([start])
    visited = {start: 0}
    while frontier:
        seq = frontier.popleft()
        for i in range(len(seq)):
            newString = click(i,seq)
            if newString == target:
                return str(visited[seq] + 1)
            if newString not in visited:
                visited[newString] = visited[seq] + 1
                frontier.append(newString)
    return "impossible"
    
start,target = input().strip(),input().strip()
print(solve(start,target))

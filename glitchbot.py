from sys import stdin

#NESW
orientation = [(0,1),(1,0),(0,-1),(-1,0)]
instr = {"Left", "Forward", "Right"}

def solve(instructions,n,x,y):
    for i in range(n):
        original = instructions[i]
        for target in instr:
            sx,sy,curr = 0,0,0
            if target != original:
                instructions[i] = target
                for movement in instructions:
                    if movement == "Left":
                        curr = (curr - 1) % 4
                    elif movement == "Right":
                        curr = (curr + 1) % 4
                    else:
                        a,b = orientation[curr]
                        sx += a
                        sy += b
                if (sx,sy) == (x,y):
                    return f"{i + 1} {target}"
        instructions[i] = original
    
x,y = map(int,stdin.readline().split())
n = int(stdin.readline())
instructions = [stdin.readline().strip() for _ in range(n)]
print(solve(instructions,n,x,y))

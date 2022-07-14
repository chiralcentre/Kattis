from sys import stdin,stdout

def generate_collatz(n):
    global numbers,step1,step2,C
    step = 0
    while True:
        if n not in numbers:
            numbers[n] = step
        else:
            step1 = numbers[n] #dictionary keeps track of previous moves
            step2 = step
            C = n
            return
        if n == 1: return
        n = 3*n + 1 if n%2 else n//2
        step += 1

while True:
    A,B = map(int,stdin.readline().split())
    if A == B == 0:
        break
    numbers,step1,step2,C = {},0,0,1
    generate_collatz(A); generate_collatz(B)
    stdout.write(f"{A} needs {step1} steps, {B} needs {step2} steps, they meet at {C}\n")
    
    

from itertools import product

def checkfours(n,operations):
    for a,b,c in operations:
        expression = f"4 {a} 4 {b} 4 {c} 4"
        if eval(expression) == n:
            return f"{expression.replace('//','/')} = {n}"
    return "no solution"
    
operations = list(product(['+','-','*','//'],repeat=3))

for _ in range(int(input())):
    num = int(input())
    print(checkfours(num,operations))

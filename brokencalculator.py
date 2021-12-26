n = int(input())
result = 1
for i in range(n):
    command = input().strip().split()
    a,op,b = int(command[0]),command[1],int(command[2])
    if op == '*':
        result = (a*b)**2
    elif op == '/':
        result = a//2 if not a%2 else (a+1)//2
    elif op == '+':
        result = a + b - result
    elif op == '-':
        result *= (a - b)
    print(result)
        

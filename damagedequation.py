a,b,c,d = list(map(int,input().split()))
operators = {0:'+',1:'-',2:'*',3:'/'}
LHS,RHS = [a+b,a-b,a*b],[c+d,c-d,c*d]
if b != 0:
    LHS.append(a//b)
if d != 0:
    RHS.append(c//d)
    
expressions = []

for i in range(len(LHS)):
    for j in range(len(RHS)):
        if LHS[i] == RHS[j]:
            expressions.append(f'{a} {operators[i]} {b} = {c} {operators[j]} {d}')
            
if len(expressions) > 0:
    for expr in sorted(expressions):
        print(expr)
else:
    print('problems ahead')

        

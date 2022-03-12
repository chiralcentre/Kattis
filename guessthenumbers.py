from sys import stdin,stdout
from itertools import permutations
from operator import add,sub,mul

def precedence(char):
    if char == '+' or char == '-':
        return 1
    elif char == '*' or char == '/':
        return 2
    elif char == '^': #exponentiation
        return 3
    else:
        return 0

def convert_to_post(expr):
    ops,result,temp = {'+','-','*'},[],[]
    #O(N) to convert to result expression,where N is number of unknowns
    for char in expr:
        if char.isalpha(): #lowercase alphabet characters
            result.append(char)
        elif char == '(':
            temp.append(char)
        elif char == ')':
            while temp and temp[-1] != '(':
                result.append(temp.pop()) #store and pop until ( has been found
            temp.pop() #remove '(' from stack
        elif char in ops:
            if precedence(char) > precedence(char[-1]):
                temp.append(char) #add if precedence is higher
            else:
                while temp and precedence(char) <= precedence(temp[-1]):
                    result.append(temp.pop()) #store and pop until higher precedence is found
                temp.append(char)
    while temp: #add any remaining operator 
        result.append(temp.pop())
    return result

def evaluate(n,expr,arrangements,m):
    ops = {'+' : add,'-' : sub,'*' : mul}
    postfix = convert_to_post(expr)
    for p in arrangements:  #O(N!)
        counter,s1 = 0,[] # stacks
        for char in postfix:
            if char.isalpha():
                s1.append(p[counter])
                counter += 1
            else: #operator
                a,b = s1.pop(),s1.pop()
                s1.append(ops[char](b,a)) # b,a is in this order to account for subtraction    
        if s1[0] == m:
            return "YES"
    return "NO"    
   
while True:
    n,*unknowns,m = list(map(int,stdin.readline().split()))
    if n == 0: break
    expr = stdin.readline().strip()
    stdout.write(evaluate(n,expr,permutations(unknowns),m)+'\n')

from sys import stdin,stdout
from fractions import Fraction as F
from math import gcd


def lcm(a,b):
    return a * b // gcd(a,b)


# runs in O(N^3) with partial pivoting
# credits to https://www.javatpoint.com/gaussian-elimination-in-python
def gauss_elim(mat):  
    num = len(mat)  
    for i in range(0, num):  
        # Searching the maximum value of a particular column  
        max_el = abs(mat[i][i])  
        # Row having the element of maximum value  
        max_row = i  
        for k in range(i + 1, num):  
            if abs(mat[k][i]) > max_el:  
                max_el = abs(mat[k][i])  
                max_row = k  
        # Swapping the maximum row with the current row   
        for k in range(i, n + 1):  
            temp = mat[max_row][k]  
            mat[max_row][k] = mat[i][k]  
            mat[i][k] = temp  
        # Chaning the value of the rows below the current row to 0   
        for k in range(i + 1, n):  
            curr = -mat[k][i] / mat[i][i]  
            for j in range(i, n + 1):  
                if i == j:  
                    mat[k][j] = 0  
                else:  
                    mat[k][j] += curr * mat[i][j]  
    # Solving the equation Ax = b for the created upper triangular matrix mat  
    l = [0 for i in range(n)]  
    for j in range(n - 1, -1, -1):  
        l[j] = mat[j][n] / mat[j][j]  
        for k in range(j - 1, -1, -1):  
            mat[k][n] -= mat[k][j] * l[j]  
    return l  

LHS,RHS,mappings,reverseMappings,counter = [],[],{},{},0
for line in stdin:
    line = line.split()
    if line[0] == line[1] == "0":
        break
    freq = {}
    for i in range(2,len(line),2):
        elem,f = line[i],int(line[i + 1])
        if elem not in mappings:
            mappings[elem] = counter
            reverseMappings[counter] = elem
            counter += 1
        freq[elem] = f if elem not in freq else freq[elem] + f
    LHS.append(freq) if line[0] == "+1" else RHS.append(freq)

#let n be dimensions of matrix
n = len(LHS) + len(RHS)
A = [[F(0) for i in range(n)] for j in range(n)]
A[0][0] = 1
for i in range(1,n):
    elem = reverseMappings[i - 1]
    for j in range(n):
        if j < len(LHS):
            temp = LHS[j]
            A[i][j] = F(temp[elem]) if elem in temp else F(0)
        else:
            temp = RHS[j - len(LHS)]
            A[i][j] = F(-temp[elem]) if elem in temp else F(0)
for i in range(n):
    A[i].append(F(0))
A[0][-1] = F(1)
coeff = gauss_elim(A)
# find LCM of denominators of fractions, and multiply all coefficients by that LCM
below_one = [c.denominator for c in coeff if c.numerator % c.denominator]
if not below_one:
    stdout.write(" ".join(str(c.numerator) for c in coeff))
else:
    LCM = 1
    for i in range(len(below_one)):
        LCM = lcm(LCM,below_one[i])
    stdout.write(" ".join(str((c * LCM).numerator) for c in coeff))
    

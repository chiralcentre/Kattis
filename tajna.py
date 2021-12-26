from math import sqrt

def find_dim(n):
    for r in range(int(sqrt(n)),0,-1):
        if not n%r:
            return (r,n//r)

def transpose(m):
    return [m[j][i] for i in range(len(m[0])) for j in range(len(m))]

message = list(input().strip())
matrix = []

N = len(message)
R,C = find_dim(N)

for i in range(C):
    matrix.append(message[0:R])
    message = message[R:]
          
invertedmat = transpose(matrix)

string = ''
for lst in invertedmat:
    for char in lst:
        string += char
print(string)

def value(r,c,n):
    v = 1
    while n > 1:
        if r >= n//2 and c >= n//2:
            v *= -1
        r %= n//2
        c %= n//2
        n //=2
    return v
        

for i in range(int(input())):
    n,x,y,w,h = list(map(int,input().split()))
    dim = n
    for i in range(y,y+h):
        for j in range(x,x+w):
            print(value(j,i,n), end = ' ')
        print() #newline
            


'''
def deepMap(f,seq):
    if seq == []:
        return seq
    elif type(seq) != list:
        return f(seq)
    else:
        return [deepMap(f,x) for x in seq]

def Hadamard(n): #n is a power of 2
    if n == 1:
        return [1]
    elif n == 2:
        return [[1,1],[1,-1]]
    else:    
        k = 2
        array = [Hadamard(k)]
        while k < n:
            k *= 2
            matrix,prev = [],array.pop(0)
            for i in range(k):
                if i < k//2:
                    matrix.append(prev[i]+prev[i])
                else:
                    matrix.append(prev[i%(k//2)]+deepMap(lambda x: -x,prev[i%(k//2)]))
            array.append(matrix)
            #print(f'matrix {k} = {matrix}')
        return array[0]
        

num = int(input())
for i in range(num):
    n,x,y,w,h = list(map(int,input().split()))
    while x + h < n//2 and y + w < n//2:
        n//=2
    mat = Hadamard(n)
    result = []
    for i in range(len(mat)):
        row = []
        for j in range(len(mat[0])):
            if x <= i <= x + h - 1 and y <= j <= y + w - 1:
                row.append(mat[i][j])
        if row:
            result.append(row)
    for lst in result:
        print(' '.join(map(str,lst)))
'''            

        

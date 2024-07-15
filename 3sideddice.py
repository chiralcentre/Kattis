from sys import stdin,stdout
from copy import deepcopy

def isSuitableSolution(A):
    for i in range(3):
        if A[i][3] <= 0:
            return False
    return True

def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def equal(a, b): # floating point issue
    return abs(a-b) < 1e-7

def leading_entry_col(A, r): # given A[r], what's the first nonzero index/column
    row,i = A[r],0
    while i < len(A[0]) and equal(row[i], 0):
        i += 1
    return i

def list_pivots(A):
    res = []
    for r in range(len(A)):
        k = leading_entry_col(A, r)
        if k != len(A[0]):
            res.append((r, k))
    res.sort(reverse = True)
    return res

def col(A, i):
    return list(map(lambda x: x[i], A))

def ero1(A, i, c): # cRi, modifies A
    for j in range(len(A[0])): A[i][j] *= c

def ero2(A, i, j, c): # Ri + cRj, modifies A
    for k in range(len(A[0])): A[i][k] += c*A[j][k]

def ero3(A, i, j): # swap Ri and Rj, modifies A
    A[i], A[j] = A[j], A[i]

def rref(A): # modifies A and returns the RREF of A
    # start from A_{1,1}
    curr_col = 0
    curr_row = 0
    while curr_col < len(A[0]) and curr_row < len(A): # while the pointer points to an entry in the matrix
        if equal(A[curr_row][curr_col], 0): # current entry is 0, we want to make it 1 by swapping with a non-zero entry
            check_col = col(A, curr_col)[curr_row+1:] # check all the entries below it
            for i in range(len(check_col)):
                if not equal(check_col[i], 0): break
                elif i == len(check_col)-1: i += 1
            if i < len(check_col): # if found a non-zero entry in that column, swap with that row
                ero3(A, curr_row, curr_row+i+1)
            else: # otherwise, all the entries in that column is zero, move on to the next column
                curr_col += 1
        else: # the entry is nonzero, do ero1 and/or ero2
            # make the current entry 1 first by doing ero1
            # now, A[curr_row][curr_col] = 1
            if not equal(A[curr_row][curr_col], 1):
                ero1(A, curr_row, 1/A[curr_row][curr_col])
            # for all rows below it, do ero2
            for i in range(curr_row + 1, len(A)):
                if not equal(A[i][curr_col], 0):
                    ero2(A, i, curr_row, -A[i][curr_col])
            curr_col += 1
            curr_row += 1
    # Now that it's all REF, let's bring it to RREF!
    pivots = list_pivots(A) # work from bottom to top
    for i in range(len(pivots)-1):
        for j in range(pivots[i][0]-1, -1, -1): # j < pr[i][0]
            ero2(A, j, pivots[i][0], -A[j][pivots[i][1]])
    return A

while True:
    first_row = list(map(int, stdin.readline().split()))
    if first_row == [0,0,0]:
        break
    A = [first_row]
    for i in range(2):
        A.append(list(map(int, stdin.readline().split())))
    b = list(map(int, stdin.readline().split()))
    # read in empty line
    stdin.readline()
    # transpose matrix
    A = transpose(A)
    for i in range(3):
        A[i].append(b[i]) # make augmented matrix
    A = rref(A)
    pv = list_pivots(A)
    if pv:
        # last column is pivot column -> inconsistent
        if pv[0][1] == 3:
            stdout.write("NO\n")
        # every column is a pivot column
        elif len(pv) == 3:
            # check if sum of solutions = 1 and a,b,c > 0
            # sum of solutions = 1 given how the system of equations is formed
            stdout.write("YES\n") if isSuitableSolution(A) else stdout.write("NO\n")
        # only columns that are pivot columns have solutions
        # multiple solutions exist
        # in case where multiple solutions exist, check if there is a triple (a,b,c) such that a + b + c = 1, 0 < a,b,c < 1
        # a + b + c = 1 is guaranteed by how the system of equations is formed
        # only need to check for 0 < a,b,c < 1
        elif len(pv) == 1:
            stdout.write("YES\n")
        elif len(pv) == 2: # rank 2
            solved = False
            # for variable c, iterate from 0.0001 to 0.9998 with steps of 0.0001
            # smallest step is 0.0001 since 10000 * 0.0001 = 1
            # upper bound is 0.9998 since a,b >= 0.0001
            k = 0.0001
            while k < 0.9999:
                B = deepcopy(A)
                B[-1] = [0,0,1,k]
                B = rref(B)
                pv2 = list_pivots(B)
                if len(pv2) == 3 and isSuitableSolution(B):
                    solved = True
                    break
                k += 0.0001
            stdout.write("YES\n") if solved else stdout.write("NO\n")              
    else:
        stdout.write("NO\n")

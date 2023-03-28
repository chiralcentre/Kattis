from sys import stdin,stdout

def findLCPLength(A,B):
    prev = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            return prev
        prev += 1
    return prev

def findLCSLength(A,B):
    prev = 0
    for i in range(len(A) - 1, -1, -1):
        if A[i] != B[i]:
            return prev
        prev += 1
    return prev

def checkReverseEqual(s,e,A,B):
    for i in range(e + 1 - s):
        if A[s + i] != B[e - i]:
            return False
    return True
    
A = stdin.readline().strip()
B = stdin.readline().strip()
#s,e represent the start and end indices of substrings in both strings that differ
s,e = findLCPLength(A,B), len(A) - 1 - findLCSLength(A,B)

#check if A[s:e+1] reversed is equal to B[s:e]
if checkReverseEqual(s,e,A,B):
    counter = 1
    s -= 1; e += 1
    while s >= 0 and e < len(A) and A[s] == A[e]:
        counter += 1
        s -= 1; e += 1
    stdout.write(f"{counter}\n")
else:
    stdout.write("0\n")

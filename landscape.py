from sys import stdin,stdout

n,k = map(int,stdin.readline().split())
#D[i] = h(i) - h(i - 1), where h(i) = height of point i
#D2[i] = S(i) - S(i - 1), where S(i) = slope of point i
#0 is provided as a sentinel value
#D records the changes made by raise/depress operations
#D2 records the second order derivative changes made by hill/valley operations
D = [0 for _ in range(n + 2)]
D2 = [0 for _ in range(n + 3)]
for _ in range(k):
    c,x1,x2 = stdin.readline().split()
    x1,x2 = int(x1),int(x2)
    if c == "R":
        D[x1] += 1
        D[x2 + 1] -= 1
    elif c == "D":
        D[x1] -= 1
        D[x2 + 1] += 1
    elif c == "H":
        p = (x2 - x1) // 2
        if not (x2 - x1) % 2: # odd
            D2[x1 + p + 1] -= 2
        else:
            D2[x1 + p + 1] -= 1
            D2[x1 + p + 2] -= 1
        D2[x1] += 1
        D2[x2 + 2] += 1
    else:
        p = (x2 - x1) // 2
        if not (x2 - x1) % 2: # odd
            D2[x1 + p + 1] += 2
        else:
            D2[x1 + p + 1] += 1
            D2[x1 + p + 2] += 1
        D2[x1] -= 1
        D2[x2 + 2] -= 1        

A = [0]
for i in range(1,len(D2)):
    A.append(A[-1] + D2[i])
# H1 contains height contributions from hills/valleys
# H2 contains height contributions from raises/depresses
H1 = [0]
for i in range(1,len(A)):
    H1.append(H1[-1] + A[i])
H2 = [0]
for i in range(1,len(D)):
    H2.append(H2[-1] + D[i])
for i in range(1,n + 1):
    stdout.write(f"{H1[i] + H2[i]}\n")

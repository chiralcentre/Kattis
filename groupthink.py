from sys import stdin

# code runs in O(n^3)
def check_associative(n,adjMat):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if adjMat[adjMat[i][j]][k] != adjMat[i][adjMat[j][k]]:
                    return False
    return True

def check_identity_and_inverse(n,adjMat):
    identity = None
    for i in range(n):
        if all([adjMat[j][i] == adjMat[i][j] == j for j in range(n)]):
            identity = i
            break
    if identity == None:
        return False,False
    for i in range(n):
        found = False
        for j in range(n):
            if adjMat[i][j] == adjMat[j][i] == identity:
                found = True
                break
        if not found:
            return True,False
    return True,True
                

n = int(stdin.readline())
adjMat = [[0 for i in range(n)] for j in range(n)]
for _ in range(n**2):
    x,y,z = map(int,stdin.readline().split())
    adjMat[x][y] = z

is_associative = check_associative(n,adjMat)
is_identity,is_inverse = check_identity_and_inverse(n,adjMat)
if is_associative:
    if is_identity and not is_inverse:
        print("monoid")
    elif is_identity and is_inverse:
        print("group")
    else:
        print("semigroup")
else:
    print("magma")

from math import factorial
#P(value >= R) = (S-R+1)/S
#Let number of rolls where value >= R = N
#P(N >= X) = P(N = X) + P(N = X+1) + ... P(N = Y)
#P(N = i) = [Y choose i]*(P(value >= R))**i*(1-P(value >= R))**(n-i) for all i
#Expected return = P(N >= X)*(WB-B) + (1-P(N >= X))*(-B) where B is initial bet 
#B can be 1 WLOG => Expected return = P(N >= X)*W - 1
def combinations(N,r):
    return factorial(N)//(factorial(N-r)*factorial(r))

def bobbybet(R,S,X,Y,W):
    p1 = (S-R+1)/S #p1 = P(value >= R)
    p2 = sum(combinations(Y,r)*p1**r*(1-p1)**(Y-r) for r in range(X,Y+1)) #p2 = P(N >= X)
    expected = p2*W - 1
    return "yes" if expected > 0 else "no"

for _ in range(int(input())):
    R,S,X,Y,W = map(int,input().split())
    print(bobbybet(R,S,X,Y,W))

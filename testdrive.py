def testdrive(a,b,c):
    if a < b < c or a > b > c:
        return "cruised" if abs(b - a) == abs(c - b) else "accelerated" if abs(b - a) < abs(c - b) else "braked"
    else:
        return "turned"

a,b,c = map(int,input().split())
print(testdrive(a,b,c))

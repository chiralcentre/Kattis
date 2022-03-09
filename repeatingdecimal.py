from sys import stdin,stdout
# returns a/b with c decimal digits with O(c) time complexity
def decimal_representation(a,b,c):
    integer_part,decimal_part = a//b,[]
    n = a - b*(integer_part)
    for i in range(c):
        n *= 10
        decimal_part.append(str(n//b))
        n -= b*(n//b)
    return str(integer_part) + '.' + ''.join(decimal_part)

for line in stdin:
    a,b,c = map(int,line.split())
    stdout.write(decimal_representation(a,b,c)+'\n')

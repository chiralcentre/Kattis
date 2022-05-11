from sys import stdin,stdout
#Successor(p/q) = q/((2*floor(p/q) + 1) * q - p)) for all cases
for _ in range(int(stdin.readline())):
    K,f1 = stdin.readline().split()
    p,q = map(int,f1.split('/'))
    succNum = q; succDenom = (2*(p//q)+1)*q - p
    stdout.write(f'{K} {succNum}/{succDenom}\n')

from sys import stdin,stdout

# I is modular multiplicative inverse of A under M
# y = (A * x + B) % M
# y - B = A * x (mod M)
# (y - B) * I = x (mod M)
M = pow(2,64)
A,B,I = 230309227,68431307,881051043651
for _ in range(100):
    y = int(stdin.readline())
    x = (y - B) * I % M
    assert 0 <= x <= pow(10,18)
    assert (x * A + B) % M == y
    stdout.write(f"{x}\n")

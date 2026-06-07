from sys import stdin,stdout

def get_res(s):
    return chr(ord('A') + sum(ord(char) - ord('A') for char in s) % 26)

def loop_write(char,f,newline=False):
    for _ in range(f):
        stdout.write(char)
    if newline:
        stdout.write("\n")
        
res = get_res(stdin.readline().strip())
shape = stdin.readline().strip()
D = int(stdin.readline())
B = (D - 1) // 2
L = 2 - D % 2
if shape == "+":
    for i in range(B):
        loop_write(" ",B)
        loop_write(res,L)
        loop_write(" ",B,True)
    for _ in range(L):
        loop_write(res,D,True)
    for i in range(B):
        loop_write(" ",B)
        loop_write(res,L)
        loop_write(" ",B,True)
elif shape == "-":
    for i in range(B):
        loop_write(" ",D,True)
    for _ in range(L):
        loop_write(res,D,True)
    for i in range(B):
        loop_write(" ",D,True)
elif shape == "x":
    for i in range(B):
        loop_write(" ",i)
        loop_write(res,L)
        loop_write(" ",D - 2 * i - 2)
        loop_write(res,L)
        loop_write(" ",i,True)
    for _ in range(L):
        loop_write(" ",B)
        loop_write(res,L * L)
        loop_write(" ",B,True)
    for i in range(B):
        loop_write(" ",B - i - 1)
        loop_write(res,L)
        loop_write(" ",D - 2 * B + 2 * i)
        loop_write(res,L)
        loop_write(" ",B - i - 1,True)
else:
    for i in range(D):
        loop_write(" ",D - i - 1)
        loop_write(res,L)
        loop_write(" ",i,True)

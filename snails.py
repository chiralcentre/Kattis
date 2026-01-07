from sys import stdin,stdout

H = pow(2,32)
L = [0,1,2,3]
while L[-4] + L[-3] + L[-2] + L[-1] < H:
    L.append(L[-4] + L[-3] + L[-2] + L[-1])
# maximum length of L is 36
# code runs in O(n) time
for _ in range(int(stdin.readline())):
    seq = stdin.readline().split()
    if len(seq) > len(L):
        stdout.write("SNAIL\n")
    else:
        for i in range(len(seq)):
            if int(seq[i]) != L[i]:
                stdout.write("SNAIL\n")
                break
        else:
            stdout.write("NAUTILUS\n")

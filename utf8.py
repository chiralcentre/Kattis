from sys import stdin

def invalid():
    print("invalid")
    exit(0)
    
n = int(stdin.readline())
b = [stdin.readline().strip() for _ in range(n)]
i,ans = 0,[0 for _ in range(4)]
while i < n:
    if b[i].startswith("0"):
        ans[0] += 1
        i += 1
    elif b[i].startswith("110"):
        if i + 1 >= n or not b[i+1].startswith("10"):
            invalid()
        ans[1] += 1
        i += 2
    elif b[i].startswith("1110"):
        if i + 2 >= n or not b[i+1].startswith("10") or not b[i+2].startswith("10"):
            invalid()
        ans[2] += 1
        i += 3
    elif b[i].startswith("11110"):
        if i + 3 >= n or not b[i+1].startswith("10") or not b[i+2].startswith("10") or not b[i+3].startswith("10"):
            invalid()
        ans[3] += 1
        i += 4
    else:
        invalid()
print("\n".join(str(num) for num in ans))

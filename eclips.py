words = input().split()
ans = [w for w in words if "e" in w]
if ans:
    print(" ".join(ans))
else:
    print("oh noes")

N = int(input())
s = input().strip()
output,seen = [],set()
for i in range(len(s)):
    seen.add(s[i])
    if len(seen) == 3:
        output.append(s[i])
        seen = set()
    if len(output) == N:
        break
print("".join(output))

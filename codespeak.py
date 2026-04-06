from sys import stdin

vowels = {"a", "e", "i", "o", "u"}

stdin.readline()
words = stdin.readline().split()
ans = []
for w in words:
    output,seen = [],False
    for char in w:
        if char in vowels:
            if not seen:
                output.append("ib")
            seen = True
        else:
            seen = False
        output.append(char)
    ans.append("".join(output))
print(" ".join(ans))

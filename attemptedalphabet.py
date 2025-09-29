letters = set(input().strip())
missing = []
for i in range(97,123):
    char = chr(i)
    if char not in letters:
        missing.append(char)
if missing:
    print("".join(missing))
else:
    print("Good job!")

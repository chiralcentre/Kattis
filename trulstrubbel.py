s = input().strip()
curr = {"T": 0, "H": 0}
other = {"T": "H","H": "T"}
for char in s:
    curr[char] += 1
    if curr[char] >= 11 and curr[char] - curr[other[char]] >= 2:
        curr = {"T": 0, "H": 0}
print(f"{curr['T']}-{curr['H']}")
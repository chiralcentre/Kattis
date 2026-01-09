from sys import stdin

counter = {"R": 0, "O": 0, "Y": 0, "G": 0, "P": 0}
skittles = stdin.readline().strip()
for char in skittles:
    counter[char] += 1
for key in list(counter.keys()):
    if counter[key] == 0:
        counter.pop(key)
for i in range(5,0,-1):
    if len(counter) != i:
        print("0")
    else:
        L,colours = pow(10,9),""
        for key, val in counter.items():
            L = min(L, val)
            colours += key
        print(f"{L} {colours}")
        for key in list(counter.keys()):
            counter[key] -= L
            if counter[key] == 0:
                counter.pop(key)
        

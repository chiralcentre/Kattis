from sys import stdin,stdout

string = stdin.readline().strip()
letters = {}
for char in string:
    letters[char] = 1 if char not in letters else letters[char] + 1
# sort by frequency in ascending order
lst = sorted(list(letters.items()), key = lambda x: x[1])
if len(lst) <= 2:
    stdout.write("0")
else:
    counter = sum(lst[i][1] for i in range(0,len(lst)-2)) # remove letters with lowest frequency
    stdout.write(f"{counter}")

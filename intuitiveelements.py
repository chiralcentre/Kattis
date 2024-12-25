from sys import stdin,stdout

def solve(original,abbrev):
    original_letters = set(original)
    for letter in abbrev:
        if letter not in original_letters:
            return "NO"
    return "YES"

for _ in range(int(stdin.readline())):
    original = stdin.readline().strip()
    abbrev = stdin.readline().strip()
    stdout.write(f"{solve(original,abbrev)}\n")

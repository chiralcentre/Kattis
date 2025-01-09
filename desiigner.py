from sys import stdin

vowels = {"a","e","i","o","u","y"}

def solve(word):
    if len(word) < 4 or word[0] != 'b':
        return "Neibb"
    i = 1
    while i < len(word) and word[i] == "r":
        i += 1
    if i < 3:
        return "Neibb"
    return "Jebb" if len(word) == i + 1 and word[i] in vowels else "Neibb"


word = stdin.readline().strip()
print(solve(word))

from sys import stdin

# Guess “abcde”, “fghij”, “klmno”, “pqrst”,”uvwxy”. 
# Using these 5 guesses, we know exactly which letters are in the squirdle.

def solve():
    guesses = ["abcde", "fghij", "klmno", "pqrst", "uvwxy"]
    ans,letters = ["" for i in range(5)],[]
    for g in guesses:
        print(f"? {g}")
        pos = input().strip()
        if pos == "22222":
            return
        for i in range(5):
            if pos[i] != "0":
                letters.append(g[i])
    # only four letters, remaining letter must be z
    if len(letters) == 4:
        letters.append("z") 
    # Guess 4 rotations of a string containing all 5 letters.
    # Since each letter has been guessed in 4 locations, we either already guessed it once at its correct location, or the location we have not guessed yet is the correct one.
    g = "".join(char for char in letters)
    explored = {char: [] for char in letters}
    for i in range(4):
        print(f"? {g}")
        pos = input().strip()
        if pos == "22222":
            return
        for j in range(5):
            if pos[j] == "2":
                ans[j] = g[j]
            else:
                explored[g[j]].append(j)
        g = g[1:] + g[0]
    for char in explored:
        if char not in ans:
            p = {0,1,2,3,4}
            for num in explored[char]:
                p.remove(num)
            p = list(p)
            ans[p[0]] = char
    s = "".join(char for char in ans)
    print(f"? {s}")
    # all characters are guaranteed to be in the correct position now
    input()
    return

if __name__ == "__main__":
    solve()

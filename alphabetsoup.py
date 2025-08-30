from sys import stdin

def solve():
    alphabet = [chr(65 + i) for i in range(26)]
    letters = stdin.readline().strip()
    unique = set()
    for char in letters:
        unique.add(char)
        if len(unique) == 26:
            print("Alphabet Soup!")
            return
    if len(unique) == 26:
        print("Alphabet Soup!")
    else:
        for letter in alphabet:
            if letter not in unique:
                print(letter,end = "")

if __name__ == "__main__":
    solve()

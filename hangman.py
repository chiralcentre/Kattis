def hangman(unique_letters,alphabet):
    wrong_moves = 0
    for i in range(26):
        if alphabet[i] in unique_letters:
            unique_letters.remove(alphabet[i])
        else:
            wrong_moves += 1
        if not unique_letters: #empty:
            return "WIN"
        if wrong_moves >= 10:
            return "LOSE"

unique_letters = set(input().strip())
alphabet = input().strip()
print(hangman(unique_letters,alphabet))


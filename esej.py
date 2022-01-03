A,B = map(int,input().split())
unique_words = []
alphabet = list("abcdefghijklmnopqrstuvwxyz")

for i in range(B//2 + 1):
    word = ''
    if i == 0:
        word += 'a'
    while i > 0:
        word += alphabet[i%26]
        i //= 26
    unique_words.append(word)

if A > B//2 + 1:
    diff = A - B//2 - 1
    reps = diff//(B//2+1)
    cutoff = diff%(B//2+1)
    essay = unique_words + reps*unique_words + unique_words[:cutoff]
    print(' '.join(essay))
else:
    print(' '.join(unique_words))

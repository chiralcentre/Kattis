s = input().strip()
word_length = len(s)//3
possible_words = {}
for i in range(0,len(s),word_length):
    possible_words[s[i:i+word_length]] = 1 if s[i:i+word_length] not in possible_words else possible_words[s[i:i+word_length]] + 1

print('\n'.join(word for word in possible_words if possible_words[word] >= 2))

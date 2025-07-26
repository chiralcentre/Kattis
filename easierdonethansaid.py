from sys import stdin,stdout

vowels = {"a", "e", "i", "o", "u"}

def is_acceptable(pwd):
    curr_vowels,curr_consonants = 0,0
    has_vowel = False
    if pwd[0] in vowels:
        curr_vowels += 1
        has_vowel = True
    else:
        curr_consonants += 1
    for i in range(1,len(pwd)):
        if pwd[i] == pwd[i - 1] and pwd[i] not in {"e", "o"}:
            return f"<{pwd}> is not acceptable."
        # four cases
        if pwd[i - 1] not in vowels and pwd[i] not in vowels:
            curr_consonants += 1
        elif pwd[i - 1] not in vowels and pwd[i] in vowels:
            curr_vowels = 1
            curr_consonants = 0
            has_vowel = True
        elif pwd[i - 1] in vowels and pwd[i] not in vowels:
            curr_consonants = 1
            curr_vowels = 0
            has_vowel = True
        elif pwd[i - 1] in vowels and pwd[i] in vowels:
            curr_vowels += 1
            has_vowel = True
        if curr_vowels >= 3 or curr_consonants >= 3:
            return f"<{pwd}> is not acceptable."
    return f"<{pwd}> is acceptable." if has_vowel else f"<{pwd}> is not acceptable."
    
while True:
    word =  stdin.readline().strip()
    if word == "end":
        break
    stdout.write(f"{is_acceptable(word)}\n")

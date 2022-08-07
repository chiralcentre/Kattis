def check(chars,words):
    if len(chars) != len(words):
        return "False"
    chartoword,wordtochar = {},{}
    for i in range(len(chars)):
        c,w = chars[i],words[i]
        if c in chartoword:
            if chartoword[c] != w:
                return "False"
        else:
            chartoword[c] = w
        if w in wordtochar:
            if wordtochar[w] != c:
                return "False"
        else:
            wordtochar[w] = c
    return "True"

chars = input().strip()
words = input().split()
print(check(chars,words))
    

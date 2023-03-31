from sys import stdin,stdout

sub = {"at": "@", "and": "&", "one": "1", "won": "1",
       "to": "2", "too": "2", "two": "2", "for": "4",
       "four": "4", "bea": "b", "bee": "b", "be": "b",
       "sea": "c", "see": "c", "eye": "i", "oh": "o",
       "owe": "o", "are": "r", "you": "u", "why": "y"}

for _ in range(int(stdin.readline())):
    line = stdin.readline().strip()
    s = 0
    while s < len(line):
        r,uppercase = line[s],line[s].isupper()
        for i in range(4,1,-1):
            if line[s: s + i].lower() in sub:
                r = sub[line[s: s + i].lower()]
                s += i
                break
        else:
            s += 1
        stdout.write(r.upper()) if uppercase and r.isalpha() else stdout.write(r)
    stdout.write("\n")  
    

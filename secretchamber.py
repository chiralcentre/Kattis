from sys import stdin,stdout

def check(firstChar,secondChar,translations):
    if firstChar == secondChar:
        return True
    frontier,seen = [firstChar],{firstChar}
    while frontier:
        u = frontier.pop()
        if u in translations:
            for v in translations[u]:
                if v not in seen:
                    seen.add(v)
                    frontier.append(v)
                    if v == secondChar:
                        return True
    return False
    
def solve(first,second,translations):
    if len(first) != len(second):
        return "no"
    for i in range(len(first)):
        if not check(first[i],second[i],translations):                  
            return "no"
    return "yes"

m,n = map(int,stdin.readline().split())
translations = {}
for _ in range(m):
    a,b = stdin.readline().split()
    if a in translations:
        translations[a].append(b)
    else:
        translations[a] = [b]

for i in range(n):
    first,second = stdin.readline().split()
    stdout.write(f"{solve(first,second,translations)}\n")

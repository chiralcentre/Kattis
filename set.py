from sys import stdin,stdout

def checkIfCardsFormSet(c1,c2,c3):
    for i in range(len(c1)):
        unique = {c1[i],c2[i],c3[i]}
        if len(unique) == 2:
            return False
    return True

cards = [item for _ in range(4) for item in stdin.readline().split()]
result = []
for i in range(len(cards)):
    for j in range(i + 1, len(cards)):
        for k in range(j + 1, len(cards)):
            if checkIfCardsFormSet(cards[i],cards[j],cards[k]):
                result.append((i + 1, j + 1, k + 1))
stdout.write("\n".join(f"{x} {y} {z}" for x,y,z in result)) if result else stdout.write("no sets")

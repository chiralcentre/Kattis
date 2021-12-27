def relations(first,second,notes,L):
    diff = set()
    for i in range(L):
        f,s = notes.index(first[i]),notes.index(second[i])
        d = s - f if s >= f else s + 12 - f
        diff.add(d)
    if len(diff) == 1:
        return 'Transposition'
    if first == list(reversed(second)):
        return 'Retrograde'
    note1,note2 = first[0],second[0]
    if note1 != note2:
        return 'Nonsense'
    i1 = notes.index(first[0])
    for j in range(1,L):
        c,d = notes.index(first[j]),notes.index(second[j])
        fshift1 = c - i1 if c >= i1 else c + 12 - i1
        bshift2 = i1 - d if d <= i1 else 12 - d + i1
        if fshift1 != bshift2:
            return 'Nonsense'
    return 'Inversion'
                

notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

L = int(input())
first,second = input().split(),input().split()
print(relations(first,second,notes,L)) 

'''
# alternate code for transposition
    for i in range(len(notes)):
        counter = True
        for j in range(L):
            f,s = notes.index(first[j]),notes.index(second[j])
            if (f+i)%12 != s:
                counter = False
        if counter:
            return 'Transposition'
'''

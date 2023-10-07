notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]

def gen_scale(i,notes):
    scale = [notes[i]]
    for _ in range(2):
        i += 2
        i %= len(notes)
        scale.append(notes[i])
    i += 1
    i %= len(notes)
    scale.append(notes[i])
    for _ in range(3):
        i += 2
        i %= len(notes)
        scale.append(notes[i])
    i += 1
    i %= len(notes)
    scale.append(notes[i])
    scale.append(scale[0]) # end with first note
    return scale

scales = {}
for i in range(len(notes)):
    scales[notes[i]] = set(gen_scale(i,notes))

n = int(input())
seq = set(input().strip().split())
ans = []
for s in scales:
    seen = scales[s]
    for elem in seq:
        if elem not in seen:
            break
    else:
        ans.append(s)
print(" ".join(s for s in ans)) if ans else print("none")
        

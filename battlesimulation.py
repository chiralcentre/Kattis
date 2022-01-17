monster_moves = input().strip()
counters = {'R':'S','B':'K','L':'H'}
start,n,mech_moves = 0,len(monster_moves),[]
while start < n:
    if start + 2 < n and monster_moves[start] != monster_moves[start+1] and monster_moves[start+1] != monster_moves[start+2] and monster_moves[start] != monster_moves[start+2]:
        mech_moves.append('C')
        start += 3
    else:
        mech_moves.append(counters[monster_moves[start]])
        start += 1
#join reduces time complexity compared to string concatenation   
print(''.join(mech_moves)) 


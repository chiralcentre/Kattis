def checkcards(S):
    cards = {'P': set(),'K': set(),'H': set(),'T': set()}
    for i in range(0,len(S),3):
        if int(S[i+1:i+3]) not in cards[S[i]]:
            cards[S[i]].add(int(S[i+1:i+3]))
        else:
            return "GRESKA"
    return ' '.join([str(13-len(cards['P'])),str(13-len(cards['K'])),str(13-len(cards['H'])),str(13-len(cards['T']))])

print(checkcards(input().strip()))

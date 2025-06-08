from sys import stdin

cards = {"A": 0, "2": 0, "3": 0, "4": 0,
         "5": 0, "6": 0, "7": 0, "8": 0,
         "9": 0, "10":0, "J": 0, "Q": 0,
         "K": 0}
N = int(stdin.readline())
for i in range(N):
    rank = stdin.readline().strip()[:-1]
    cards[rank] += 1
least_freq = min(cards.values())
print((4 - least_freq) / (52 - N))
        
    
    
    
    

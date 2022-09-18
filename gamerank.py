from sys import stdin,stdout

#set an arbitraily large number of wins to rank up for rank 0 (Legend)
ranksToStars = {0:100000000}
for i in range(1,26):
    ranksToStars[i] = 5 if 1 <= i <= 10 else 4 if 11 <= i <= 15 else 3 if 16 <= i <= 20 else 2 

rank,stars,consec_wins = 25,0,0
matches = stdin.readline().strip()
for char in matches:
    if char == "W":
        stars += 1
        consec_wins += 1
        if 6 <= rank <= 25 and consec_wins >= 3:
            stars += 1
        if stars > ranksToStars[rank]:
            stars -= ranksToStars[rank]
            rank -= 1
    else:
        if 1 <= rank <= 20:
            stars -= 1
            if stars < 0:
                if rank == 20:
                    stars = 0
                else:
                    rank += 1
                    stars = ranksToStars[rank] - 1
        consec_wins = 0
    #print(f"stars = {stars}, rank = {rank}, consec_wins = {consec_wins}")
stdout.write(str(rank)) if rank > 0 else stdout.write("Legend")

        
        

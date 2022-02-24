from sys import stdin,stdout

P,D = map(int,stdin.readline().split())
districts = {num: [0,0] for num in range(1,D+1)} #zero index represents votes for A, index one represents votes for B
total_votes,wasted_votes_A,wasted_votes_B = 0,0,0
for _ in range(P):
    d,A,B = map(int,stdin.readline().split())
    districts[d][0] += A
    districts[d][1] += B
    total_votes += A + B
    
for key in districts:
    v1,v2 = districts[key]
    winner = 'A' if v1 > v2 else 'B' #no tie
    w1 = v1 if winner == 'B' else v1 - (((v1+v2)//2)+1)
    w2 = v2 if winner == 'A' else v2 - (((v1+v2)//2)+1)
    wasted_votes_A += w1; wasted_votes_B += w2
    stdout.write(f'{winner} {w1} {w2}\n')
    
stdout.write(str(abs(wasted_votes_A-wasted_votes_B)/total_votes)+'\n')

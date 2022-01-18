def find_winners(scores): 
    A,B,tied = 0,0,False 
    for i in range(0,len(scores),2): 
        if scores[i] == 'A': 
            A += int(scores[i+1]) 
        else: 
            B += int(scores[i+1]) 
        if A == 10 and B == 10: 
            tied = True 
        if not tied and (A >= 11 or B >= 11): 
            return 'A' if A >= 11 else 'B' 
        if tied and abs(A-B) >= 2: 
            return 'A' if A > B else 'B' 
 
scores = input().strip() 
print(find_winners(scores))

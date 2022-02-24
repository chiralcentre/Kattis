s1,s2,s3 = ['A','B','C'],['B','A','B','C'],['C','C','A','A','B','B']
N,answers = int(input()),input().strip()
scores = {'Adrian':0,'Bruno':0,'Goran':0}
for i in range(N):
    if s1[i%len(s1)] == answers[i]:
        scores['Adrian'] += 1
    if s2[i%len(s2)] == answers[i]:
        scores['Bruno'] += 1
    if s3[i%len(s3)] == answers[i]:
        scores['Goran'] += 1
        
M = max(scores.values()); print(M)
for key,value in scores.items():
    if value == M:
        print(key)

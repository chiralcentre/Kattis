from sys import stdin,stdout

def add_to_set(k,chosen,lst):
    for i in range(k):
        chosen.add(lst[i][3])
        
N,K = map(int,stdin.readline().split())
pokenoms = []
for i in range(N):
    A,D,H = map(int,stdin.readline().split())
    pokenoms.append((A,D,H,i)) #include index of pokenom for identification purposes

chosen = set()
for i in range(3):
    pokenoms.sort(key = lambda x: x[i],reverse=True) #sort by attack,defence and attribute attribute separately in descending order, each in O(N log N) time
    add_to_set(K,chosen,pokenoms)
stdout.write(str(len(chosen)))
    


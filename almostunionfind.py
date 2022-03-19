from sys import stdin,stdout

class unionFind:
    def __init__(self,N):
        self.p2 = [i for i in range(N)] #keeps track of original parent when a move is made
        self.p = [i for i in range(N)]
        self.rank = [0 for i in range(N)]
        self.numElems = [1 for i in range(N)]
        self.total = [i for i in range(N)]
    '''
    def debug(self):
        print(f'p2 = {self.p2}')
        print(f'p = {self.p}')
        print(f'numElems = {self.numElems}')
        print(f'total = {self.total}')
    ''' 
    def findSet(self,j):
        a = self.p2[j]
        b = self.p[a]
        while a != b:
            self.p[a] = self.p[b]
            a = self.p[a]
            b = self.p[a]
        return a
        
    def isSameSet(self,i,j):
        return self.findSet(i) == self.findSet(j)

    def unionSet(self,i,j):
        if not self.isSameSet(i,j):
            x,y = self.findSet(i),self.findSet(j)
            # union by rank
            if self.rank[x] > self.rank[y]:
                x,y = y,x
            self.p[y] = x
            self.numElems[x] += self.numElems[y]
            self.numElems[y] = 0
            self.total[x] += self.total[y]
            self.total[y] = 0
        
    def move(self,a,b): 
        if not self.isSameSet(a,b):
            x,y = self.findSet(a),self.findSet(b)
            self.numElems[y] += 1
            self.numElems[x] -= 1
            self.total[y] += a
            self.total[x] -= a
            self.p2[a] = y
        
    def numberOfElems(self,i):
        return self.numElems[self.findSet(i)]

    def elemSum(self,i): # add back due to zero indexing
        return self.total[self.findSet(i)] + self.numberOfElems(i)
                            
while True:
    try:
        n,m = map(int,stdin.readline().split())
        UFDS = unionFind(n)
        for i in range(m):
            command = stdin.readline().split()
            if command[0] == '1': #-1 to offset for zero indexing
                UFDS.unionSet(int(command[1])-1,int(command[2])-1)
            elif command[0] == '2':
                UFDS.move(int(command[1])-1,int(command[2])-1)
            else: #'3' command
                stdout.write(f'{UFDS.numberOfElems(int(command[1])-1)} {UFDS.elemSum(int(command[1])-1)}\n')
    except: #EOF error
        break
    
    
    

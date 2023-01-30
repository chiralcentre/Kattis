from sys import stdin,stdout

def DFS(index,total):
    global b,a,n
    s,d,i = 1,int(a[index]),0
    while s <= total:
        if not (total - s) % 10: #total - s must be multiple of 10
            if index + 1 == n:
                if total == s:
                    return [i]
            else:
                ans = DFS(index + 1, (total - s) // 10)
                if ans: #check if list is empty, which indicates an invalid path
                    ans.append(i)
                    return ans
        i += 1; s *= d
    return []
           
    
a,b = stdin.readline().split()
n,b = len(a),int(b)
a = a[::-1]
ans = DFS(0,b)
stdout.write(" ".join(str(num) for num in ans))
    
    
    

    
    

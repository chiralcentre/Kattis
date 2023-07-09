from sys import stdin,stdout

def get_bit(num, bit):
    temp = (1 << bit) & num
    return 0 if temp == 0 else 1
        
def get_all_subsets(v, sets):
    for i in range(1 << len(v)):
      st = []
      for j in range(len(v)):
         if get_bit(i, j) == 1:
            st.append(v[j])
      sets.append(st)

#complete search in O(N * 2^N)   
N = int(stdin.readline())
indices,subsets = [i for i in range(N)],[]
get_all_subsets(indices, subsets)
ingredients = [tuple(map(int,stdin.readline().split())) for _ in range(N)]
ans = pow(10,18)
for s in subsets:
    if s:
        p,t = 1,0
        for i in s:
            p *= ingredients[i][0]
            t += ingredients[i][1]
        ans = min(ans,abs(p - t))
stdout.write(f"{ans}\n")

from sys import stdin,stdout

# since original sequence is 1st permutation in ascending order to include remaining subsequence S,
# this also means that missing subsequence S' in that permutation must be in ascending order
# merge S and S' using merge step of merge sort to get back orgiinal sequence
n,m = map(int,stdin.readline().split())
seen = [False for _ in range(n + 1)]
original = []
for i in range(m):
    x = int(stdin.readline().strip())
    seen[x] = True
    original.append(x)
missing = [i for i in range(1, n + 1) if not seen[i]]
output = [-1 for _ in range(n)]
leftIdx,rightIdx,idx = 0,0,0
#merge step
while leftIdx < len(original) and rightIdx < len(missing):
    if original[leftIdx] <= missing[rightIdx]:
        output[idx] = original[leftIdx]
        leftIdx += 1
    else:
        output[idx] = missing[rightIdx]
        rightIdx += 1
    idx += 1
while leftIdx < len(original):
    output[idx] = original[leftIdx]
    idx += 1; leftIdx += 1
while rightIdx < len(missing):
    output[idx] = missing[rightIdx]
    idx += 1; rightIdx += 1
stdout.write("\n".join(str(elem) for elem in output))
    
    

from sys import stdin,stdout

n,k = map(int,stdin.readline().split())
original,end = [i + 1 for i in range(n)], n - 1
while k > end:
    k -= end
    end -= 1
if k != 0:
    if k == end:
        k -= end
        end -= 1
    else: # k < end
        original[k],original[k - 1] = original[k - 1],original[k]
for i in range(end,n):
    original[i] = n - i + end
stdout.write(" ".join(str(pages) for pages in original))

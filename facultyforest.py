# counting components question but no need for graph traversal
# every edge is distinct and for every edge added component count decreases by 1
n,m = map(int, input().split())
print(n - m)

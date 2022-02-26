m,n = map(int,input().split())
for _ in range(m): a,b,c = map(int,input().split()) # content of clauses not important
print('unsatisfactory') if m < 8 else print('satisfactory')

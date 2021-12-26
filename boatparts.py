def theseus(n1,n2):
    parts,counter = [],0
    for i in range(n2):
        part = input().strip()
        if part not in parts:
            parts.append(part)
        if len(parts) == n1:
            return i+1
    return 'paradox avoided'

P,N = list(map(int,input().split()))
print(theseus(P,N))

n = int(input())
guests = list(map(int,input().split()))

languages = {}
for seat,l in enumerate(guests):
    if l not in languages:
        languages[l] = seat
    else:
        n = min(n,seat-languages[l])
        languages[l] = seat
print(n)


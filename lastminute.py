Au,Bu,Ar,Br = map(int,input().split())
# reusable problem statements can be used with both unique and reusable methods
def lastminute(Au,Bu,Ar,Br):
    # 16 possibilities in total
    if Au == Ar == 0 or Bu == Br == 0: #7 possibilities
        return 0
    if Au == 0 and Bu > 0 and Ar > 0 and Br > 0:
        return Ar*Br+Bu
    if Au > 0 and Bu == 0 and Ar > 0 and Br > 0:
        return Ar*Br+Au
    if Au > 0 and Bu > 0 and Ar == 0 and Br > 0:
        return Au
    if Au > 0 and Bu > 0 and Ar > 0 and Br == 0:
        return Bu
    if Au == Bu == 0 and Ar > 0 and Br > 0:
        return Ar*Br
    if Au == Br == 0 and Bu > 0 and Ar > 0:
        return Bu
    if Bu == Ar == 0 and Au > 0 and Br > 0:
        return Au
    if Ar == Br == 0 and Au > 0 and Bu > 0:
        return min(Au,Bu)
    if Au > 0 and Bu > 0 and Ar > 0  and Br > 0:
        return Br*Ar+Bu+Au   

print(lastminute(Au,Bu,Ar,Br))

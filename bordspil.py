n,m = map(int,input().split())
n += 2 # note that in the event of tie, Arnar wins
print("Arnar") if m < n - n // 3 else print("Unnar")

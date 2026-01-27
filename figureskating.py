from sys import stdin

n = int(stdin.readline())
predicted = [stdin.readline().strip() for _ in range(n)]
pred_map = {value: index for index,value in enumerate(predicted)}
final = [stdin.readline().strip() for _ in range(n)]
final_map = {value: index for index,value in enumerate(final)}
best,place,ans = -1,pow(10,9),None
for key, value in pred_map.items():
    fp = final_map[key]
    d = value - fp
    if d > best:
        best,place,ans = d,fp,key
    elif d == best and fp < place:
        place,ans = fp,key
print(ans) if best > 0 else print("suspicious")

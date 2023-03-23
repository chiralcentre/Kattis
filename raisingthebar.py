n,d = map(int,input().split())
digits,rem = 0,n % d
mp = {}
while rem != 0 and rem not in mp:
    mp[rem] = digits
    rem *= 10
    rem %= d
    digits += 1
print(f"{digits} 0") if rem == 0 else print(f"{mp[rem]} {digits - mp[rem]}")

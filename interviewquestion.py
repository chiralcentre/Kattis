from sys import stdin,stdout
import math

def gcd(lst):
    if len(lst) == 1:
        return lst[0]
    ans = lst[0]
    for i in range(1,len(lst)):
        ans = math.gcd(ans,lst[i])
    return ans

c,d = map(int,stdin.readline().split())
transcript = stdin.readline().split()
fizz,buzz = [],[]
for i in range(d - c + 1):
    if transcript[i] == "Fizz":
        fizz.append(c + i)
    elif transcript[i] == "Buzz":
        buzz.append(c + i)
    elif transcript[i] == "FizzBuzz":
        fizz.append(c + i)
        buzz.append(c + i)

a = 100001 if not fizz else gcd(fizz)
b = 100002 if not buzz else gcd(buzz)
stdout.write(f"{a} {b}\n")


def GCD(a,b):
    if a == 0:
        return b
    return GCD(b%a,a)
#a x b = LCM(a, b) * GCD (a, b)
def LCM(a,b):
    return (a*b)//GCD(a,b)
p,q,s = map(int,input().split())
print("yes") if LCM(p,q) <= s else print("no")

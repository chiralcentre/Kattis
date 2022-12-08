#let f(L,R) denote the remainder mod 9 after concatenating numbers from L to R inclusive
#remainder of number mod 9 = sum of digits mod 9
#for this reason, f(L,R) = (L + L + 1 + ... + R) % 9
#Lemma 1: sum of any 9 consecutive numbers is divisible by 9.
#Proof: Let smallest number out of the 9 consecutive numbers be a.
#Then, sum of the 9 numbers = 9a + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 9a + 36 = 9(a + 4)
#By Lemma 1, f(L,R) = f(L,R+9k) where k is an integer
#to speed up computation, reduce R by largest multiple of 9 such that the resulting value >= L

L,R = map(int,input().split())
R -= ((R - L)//9)*9
print(sum(i%9 for i in range(L,R+1))%9)


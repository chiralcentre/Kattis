sh,sm,ss = map(int,input().split(":"))
eh,em,es = map(int,input().split(":"))
h = 1 if sh < 12 and eh >= 12 else 0
m = eh - sh
s = (eh - sh) * 60 + em - sm
print(f"{h} {m} {s}")

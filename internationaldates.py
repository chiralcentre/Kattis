A,B,C = map(int,input().split("/"))
if A > 12 and B <= 12:
    print("EU")
elif A <= 12 and B > 12:
    print("US")
else:
    print("either")

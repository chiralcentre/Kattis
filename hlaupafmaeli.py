def leap_year_count(x):
    return (x >> 2) - x // 100 + x // 400
Y = int(input())
if Y % 4 or (not Y % 100 and Y % 400):
    print("Neibb")
else:
    print(leap_year_count(Y) - leap_year_count(2020))

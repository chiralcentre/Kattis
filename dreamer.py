from itertools import permutations
from sys import stdin,stdout

month_days = {1: 31, 2: 28, 3: 31, 4: 30,
              5: 31, 6: 30, 7: 31, 8: 31,
              9: 30, 10: 31, 11: 30, 12: 31}

def is_leap_year(year):
    if not year % 4:
        if year % 100:
            return True
        else:
            return not year % 400
    return False

def is_valid(d,m,y):
    if is_leap_year(y):
        month_days[2] = 29
    res = m in month_days and d <= month_days[m]
    month_days[2] = 28
    # check if 1 <= d <= month maximum, 1 <= m <= 12 and year >= 2000
    return d >= 1 and res and y >= 2000


for _ in range(int(stdin.readline())):
    digits = stdin.readline().strip().replace(" ","")
    dates = set()
    for perm in permutations(digits):
        day = int("".join(perm[:2]))
        month = int("".join(perm[2:4]))
        year = int("".join(perm[4:]))
        if is_valid(day,month,year):
            dates.add((day,month,year))
    if dates:
        sorted_dates = sorted(dates,key=lambda x: (x[2],x[1],x[0]))
        earliest = sorted_dates[0]
        earliest_day = str(earliest[0])
        if len(earliest_day) == 1:
            earliest_day = "0" + earliest_day
        earliest_month = str(earliest[1])
        if len(earliest_month) == 1:
            earliest_month = "0" + earliest_month
        stdout.write(f"{len(dates)} {earliest_day} {earliest_month} {earliest[2]}\n")
    else:
        stdout.write(f"0\n")

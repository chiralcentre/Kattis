for _ in range(int(input())):
    name,date1,date2,courses = input().split()
    y1 = list(map(int,date1.split('/')))[0]
    y2 = list(map(int,date2.split('/')))[0]
    print(f'{name} eligible') if y1 >= 2010 or y2 >= 1991 else print(f'{name} ineligible') if int(courses) > 40 else print(f'{name} coach petitions')

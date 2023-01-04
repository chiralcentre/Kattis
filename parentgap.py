import datetime

def ith_sunday(year,month,i):
    #1 + 7i is the smallest ith Sunday in the month
    ans = datetime.date(year,month, 1 + i * 7)
    #check what day is the 1 + 7i
    w = ans.weekday()
    if w != 6: #if not a Sunday, replace the day
        ans = ans.replace(day = (1 + i * 7 + (6 - w) % 7))
    return ans

y = int(input())
d1,d2 = ith_sunday(y,5,2),ith_sunday(y,6,3)
diff = d2 - d1
num_weeks = diff.days // 7 + 1 if diff.days % 7 else diff.days // 7
print(f"{num_weeks} weeks")

    

D,M = map(int,input().split())

months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
weekday = {0:'Thursday',1:'Friday',2:'Saturday',3:'Sunday',4:'Monday',5:'Tuesday',6:'Wednesday'}

days = sum(months[i] for i in range(1,M)) + D - 1 #days from 1st January
print(weekday[days%7])


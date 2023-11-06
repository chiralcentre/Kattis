angle = int(input())
# note that the hour hand moves 0.5 degrees per minute, while the minute hand moves 6 degrees per minute
for i in range(720): #there are 720 minutes in 12 hours
    h = 5 * i
    m = 60 * (i % 60)
    if (h <= m and angle == m - h) or (h > m and angle == 3600 - h + m):
        print(f"{'%02d' % (i // 60)}:{'%02d' % (i % 60)}")
        break

def distance_square(pos1,pos2):
    return (pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2

def lightacandle(book,candles,radius):
    for candle in candles:
        if distance_square(book,candle) <= radius**2:
            return 'light a candle'
    return 'curse the darkness'
        
for i in range(int(input())):
    book = tuple(map(float,input().split()))
    candles = [tuple(map(float,input().split())) for j in range(int(input()))]
    print(lightacandle(book,candles,8))

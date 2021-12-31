def earlywinter(snowfall,dm):
    for j in range(n):
        if snowfall[j] <= dm:
            return f'It hadn\'t snowed this early in {j} years!'
    return 'It had never snowed this early!'

n,dm = map(int,input().split())
snowfall = list(map(int,input().split()))
print(earlywinter(snowfall,dm))


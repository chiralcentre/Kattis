sessions = 0
for _ in range(int(input())):
    colour = input().strip().lower()
    if 'pink' in colour or 'rose' in colour:
        sessions += 1
print(sessions) if sessions > 0 else print("I must watch Star Wars with my daughter")

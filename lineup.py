print((lambda team: "INCREASING" if team == sorted(team) else "DECREASING" if team == sorted(team,reverse = True) else "NEITHER")([input().strip() for _ in range(int(input()))]))

courses = {}
for i in range(int(input())):
    frosh = tuple(sorted(map(int,input().split())))
    courses[frosh] = 1 if frosh not in courses else courses[frosh] + 1
    
print(sum([value for key,value in courses.items() if value == max(courses.values())]))

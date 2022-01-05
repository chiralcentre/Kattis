for _ in range(int(input())):
    blank_line,children = input(),int(input())
    candies = sum(int(input()) for i in range(children))
    print('NO') if candies%children else print('YES')

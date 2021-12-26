while True:
    n = int(input())
    if n == 0:
        break
    orders = {}
    for i in range(n):
        lst = input().split()
        diner,items = lst[0],lst[1:]
        for item in items:
            if item not in orders:
                orders[item] = [diner]
            else:
                orders[item].append(diner)
    for key in sorted(orders.keys()): #items need to be sorted
        print(key, ' '.join(sorted(orders[key]))) #names need to be sorted
    print() #new line

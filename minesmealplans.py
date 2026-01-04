from sys import stdin,stdout

meals = {"Marble": 19, "Marble+": 19,
         "Quartz": 14, "Quartz+": 14}
munch = {"Marble": 20000, "Marble+": 35000,
         "Quartz": 20000, "Quartz+": 35000}

for _ in range(int(stdin.readline())):
    name,plan,swipe,money = stdin.readline().split()
    swipe_count = meals[plan]
    munch_money = munch[plan]
    swipe,money = int(swipe), int(float(money) * 100)
    swipe_left,money_left = swipe_count - swipe,munch_money - money
    if swipe < swipe_count and money < munch_money:
        stdout.write(f"{name} {swipe_left} {money_left // 100}.{str(money_left % 100).zfill(2)} Use meal swipe or munch money\n")
    elif swipe == swipe_count and money < munch_money:
        stdout.write(f"{name} 0 {money_left // 100}.{str(money_left % 100).zfill(2)} Use munch money\n")
    elif swipe < swipe_count and money == munch_money:
        stdout.write(f"{name} {swipe_left} 0.00 Use meal swipe\n")
    else:
        stdout.write(f"{name} 0 0.00 Go to Downtown Golden!\n")

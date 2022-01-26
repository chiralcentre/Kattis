restaurants = []
for _ in range(int(input())):
    k = int(input())
    name = input().strip()
    menu_items = [input().strip() for _ in range(k)]
    if "pea soup" in menu_items and "pancakes" in menu_items:
        restaurants.append(name)
print(restaurants[0]) if restaurants else print("Anywhere is fine I guess")

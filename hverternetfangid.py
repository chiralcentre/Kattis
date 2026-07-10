from sys import stdin

line = stdin.readline().strip()
email = line.split(": ")[1]
user,domain = email.split("@")
first = user.split("+")[0]
print(f"{first}@{domain}")

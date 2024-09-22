seconds_conversion = {"sekundur": 1, "sekunda": 1, "minutur": 60, "minuta": 60,
                      "klukkustundir": 3600, "klukkustund": 3600, "dagar": 28800, "dagur": 28800,
                      "vikur": 144000, "vika": 144000, "ar": 7488000,
                      "daglega": 28800, "vikulega": 144000, "arlega": 7488000}
n,w,freq = input().split()
n1,t1 = input().split()
n2,t2 = input().split()
n,n1,n2 = int(n),int(n1),int(n2)
manual_time = 7488000 // seconds_conversion[freq] * n * n1 * seconds_conversion[t1] * 5
auto_time = n2 * seconds_conversion[t2]
print("Borgar sig ekki!") if auto_time > manual_time else print(manual_time - auto_time)

from sys import stdin,stdout

trip_record = {}
for i in range(int(stdin.readline())): #O(n)
    trip = stdin.readline().split()
    country,year = trip[0],int(trip[1])
    if country not in trip_record:
        trip_record[country] = [year]
    else:
        trip_record[country].append(year)

for key in trip_record: #O(k*n log n) where k = number of unique countries
    trip_record[key].sort() 
    
for j in range(int(stdin.readline())): #O(q)
    country,k = stdin.readline().split()
    stdout.write(f'{trip_record[country][int(k)-1]}\n')

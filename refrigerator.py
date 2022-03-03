from math import ceil
Pa,Ka,Pb,Kb,n = map(int,input().split())
trips_A = ceil(n/Ka)
final_cost,final_trips_A,final_trips_B = Pa*trips_A,trips_A,0
# no more than 100 iterations, since Ka >= 10 and n <= 1000
while trips_A > 0:
    trips_A -= 1
    trips_B = ceil((n - trips_A*Ka)/Kb)
    if trips_A*Pa + trips_B*Pb < final_cost:
        final_cost = trips_A*Pa + trips_B*Pb
        final_trips_A,final_trips_B = trips_A,trips_B
print(f'{final_trips_A} {final_trips_B} {final_cost}')

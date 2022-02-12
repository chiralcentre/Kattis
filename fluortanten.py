n = int(input())
children = list(map(int,input().split()))
children.remove(0)

prefix_sum_array,index_sum_array = [0 for _ in range(n-1)],[0 for _ in range(n-1)]
prefix_sum,index_sum = 0,0
# O(n) time complexity
for key,value in enumerate(children):
    prefix_sum += value
    index_sum += (key+1)*value
    prefix_sum_array[key],index_sum_array[key] = prefix_sum,index_sum

happiness = index_sum_array[n-2] #if Bjorn was inserted in last spot
#O(n) time complexity
for i in range(n-1): #insert Bjorn at every spot except last spot and calculate happiness
    #add the happiness of every children from the ith position onwards due to rightshifting of indices from insertion of Bjorn
    #sum of happiness of every children from ith position onwards,S = prefix_sum_array[n-2] - prefix_sum_array[i-1] if i > 0 else prefix_sum_array[n-2]
    S = prefix_sum_array[n-2] - prefix_sum_array[i-1] if i > 0 else prefix_sum_array[n-2]
    total = index_sum_array[n-2] + S 
    if total > happiness:
        happiness = total
        
print(happiness)
    


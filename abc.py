inpt = list(map(int, input().split()))
order = list(input())
def abc(nums, lst):
    string = ''
    sort_nums = sorted(nums)
    for value in lst:
        string += str(sort_nums[ord(value)-ord('A')]) + ' '
    return string
print(abc(inpt,order))    


#'A' - 'A' = 0, 'B' - 'A' = 1, 'C' - 'A' = 2
#1 5 3
#ABC
#--> 1 3 5
#6 4 2
#CAB
#6 2 4

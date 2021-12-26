string = input()
num = len(string)

def first_line(n):
    for i in range(n):
        print('..#.',end = '') if (i+1)%3 else print('..*.',end = '')
    print('.') 

def second_line(n):
    for j in range(n):
        print('.#.#',end = '') if (j+1)%3 else print('.*.*',end = '')
    print('.')
    
def third_line(n,s1):
    for k in range(n):
        if k == 0:
            print(f'#.{s1[k]}.',end = '')
        else:
            print(f'#.{s1[k]}.',end = '') if(k+1)%3 and k%3 else print(f'*.{s1[k]}.',end = '')
    print('#') if (k+1)%3 else print('*')


first_line(num)
second_line(num)
third_line(num,string)
second_line(num)
first_line(num)

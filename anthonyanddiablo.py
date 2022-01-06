from math import pi

A,N = map(float,input().split())
# a circle has the most area and least perimeter
print('Diablo is happy!') if N**2/(4*pi) >= A else print('Need more materials!')

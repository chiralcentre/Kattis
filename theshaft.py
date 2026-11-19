from math import sqrt

# let T represent the time taken for the rock to hit the bottom
# uT + 0.5aT^2 = (t - T)c, where u is initial velocity and a is acceleration
# u = 0, a = g
# gT^2 = 2tc - 2Tc
# gT^2 + 2cT - 2ct = 0
# use quadratic formula, take positive solution
# T = (-2c + sqrt(4c^2 + 8gct)) / 2g = (-c + sqrt(c^2 + 2gct)) / g
g,c,t = map(float,input().split())
T = (-c + sqrt(c * c + 2 * g * c * t)) / g
print((t - T) * c)

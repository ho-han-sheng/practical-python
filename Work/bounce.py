# bounce.py
#
# Exercise 1.5

height = 100
bounce_limit = int(input('Input the number of bounces:'))
x = 1

while x < bounce_limit + 1:
    height *= 0.6
    print(round(height, 4))
    x += 1

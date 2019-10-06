#假设所切割的4个角都是等腰三角形且全等
import random
def monte_carlo(n):
    i = 0
    count = 0
    w = 1
    while i <= n:
        x = random.random(0,4)
        y = random.random(0,4)
        if y >= w-x and y >= x+4-w and y > -x+8-w and y > x+w-4 :
            #为了提高精度，前取后不取
            count += 1
        i += 1
    S = 16*count/n
    print(S)

monte_carlo(1000000)

import math

for i in range(100, 401):
    j = i
    ec = 0
    while j > 0:
        rem = j%10
        if rem%2 == 0:
            ec += 1
        j = math.floor(j/10)
    if ec == 3:
        print(i)

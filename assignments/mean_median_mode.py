n = int(input())

l = []
sum = 0
for i in range(n):
    x = int(input())
    sum += x
    l.append(x)

l.sort()
median = 0
if n % 2 == 0:
    median = (l[int(n/2)] + l[int(n/2)+1]) / 2
else:
    median = l[int(n+1)/2]

print("Mean: ", sum / n)
print("Median: ", median)

# 7
# 23 98 34 29 48 49 27

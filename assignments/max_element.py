n = int(input("Enter n: "))
max = 0
for i in range(0, n):
    val = int(input())
    if(val > max):
        max = val

print(max)
l = []
n = int(input("Enter length: "))
for i in range(n):
    val = int(input())
    l.append(val)

for i in range(n-1, -1, -1):
    print(l[i], end=" ")

print()
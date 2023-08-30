l = []
n = int(input("Enter n: "))
for i in range(0, n):
    val = int(input())
    l.append(val)

print(l)
l.insert(0, l[-1])
l.pop()
print(l)

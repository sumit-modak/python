print("Enter three values: ")
x = int(input())
y = int(input())
z = int(input())

l = []
l.append(x)
l.append(y)
l.append(z)
l.sort()

print("Median value: "+ str(l[1]))

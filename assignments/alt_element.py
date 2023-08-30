l = []
n = int(input("Enter n: "))
t = int(input("Enter test cases: "))
print("Enter elements: ")
for i in range(n):
    val = int(input())
    l.append(val)

while t>1:
    c = int(input())
    print(l[~c])

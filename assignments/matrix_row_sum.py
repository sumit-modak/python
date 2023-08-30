m = int(input("Enter row size: "))
n = int(input("Enter column size: "))

mat = []
for i in range(m):
    sum = 0
    for j in range(n):
        val = int(input())
        sum += val
    mat.append(sum)

print(mat)
    
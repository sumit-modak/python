import random

n = random.randint(1, 21)
# print(n)
s = set({})
for i in range(n):
    val = random.randint(1, 21)
    s.add(val)

s.add(21)

print("The list of numbers are:")
print(s)
print("Do you want to accept the first play")
start = input("Press y to accept: ")

n = len(s)

if start == 'y' or start == 'Y':
    if n % 2 == 0:
        print("You won")
    else:
        print("You lost")
else:
    if n % 2 == 0:
        print("You lost")
    else:
        print("You won")

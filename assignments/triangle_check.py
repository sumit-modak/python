x = int(input("Enter first side length: "))
y = int(input("Enter second side length: "))
z = int(input("Enter third side length: "))

if x == y == z:
    print("equilateral triangle")
elif x != y != z:
    print("scalene triangle")
else:
    print("isosceles triangle")

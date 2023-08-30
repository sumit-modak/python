import random

num = int(input("Enter length of list: "))
low = int(input("Enter lower bound: "))
high = int(input("Enter upper bound: "))
odd_count = 0
even_count = 0

for i in range(0, num):
    x = random.randint(low, high+1)
    if x%2==0:
        even_count += 1
    else:
        odd_count += 1

print("Total odd numbers: "+str(odd_count))
print("Total even numbers: "+str(even_count))
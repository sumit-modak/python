s = input("Enter a string: ")

for i in s:
    if i.isdigit() == False:
        print("not an integer")
        exit()

print("integer")
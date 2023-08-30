s = input("Enter your string: ")

digits = 0
letters = 0

for i in s:
    if i.isdigit():
        digits += 1
    elif i.isupper() or i.islower():
        letters += 1

print("Digit count: "+str(digits))
print("Letter count: "+str(letters))

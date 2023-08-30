def toCelsius(far):
    return (5/9)*(far-32)

def toFarhenheit(cel):
    return (cel*9/5)+32

print("Press 0 for converting celsius to farhenhiet")
print("Press 1 for converting farhenhiet to celsius")
x = int(input())

if x==0:
    y = float(input("Enter temp. in celsius: "))
    print(toFarhenheit(y))
elif x==1:
    y = float(input("Enter temp. in farhenheit: "))
    print(toCelsius(y))
else:
    print("dont let me swear")
dage = float(input("Enter your dog's age: "))

# for the first two years = 10.5 and 4 each for rest of the years

def dog_age_calculator(age):
    res = 0
    if age<2:
        res = age*5.25
    else:
        res = 2 * 5.25
        res += (age - 2) * 4
    return res

hage = dog_age_calculator(dage)
print("Equivalent human age: "+str(hage))

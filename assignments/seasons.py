mon = input("Enter month: ")
day = int(input("Enter day: "))

dict = {"January": "Winter",
        "February": "Winter",
        "March": "Spring",
        "April": "Spring",
        "May": "Summer",
        "June": "Summer",
        "July": "Summer + Monsoon",
        "August": "Summer + Monsoon",
        "September": "Autumn",
        "October": "Autumn",
        "November": "Winter",
        "December": "Winter"
        }

print(dict.get(mon))
l = ["", "January", "February", "March",
     "April", "May", "June", "July",
     "August", "September", "October", 
     "November", "December"]

s = input("Enter date in mm/dd/yyyy format: ")
month = int(s[:2])

res = l[month] + " " + s[3:5] + ", " + s[6:]
print(res)
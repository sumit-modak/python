s = {1, 3, 5, 2, 4, 7, 9}
ss = {2, 5, 7}

b = True
for i in ss: 
    if i not in s:
        b = False
        break

if b == True:
    print("subset")
else:
    print("not a subset")

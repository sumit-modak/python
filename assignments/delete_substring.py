s = input("Enter string: ")
st = input("Enter substring: ")
n = len(st)
m = len(s)
res = "" 

for i in range(0, m-n):
    temp = s[i:i+n]
    if temp == st:
        res = s[:i] + s[i+n:]
        break

print(res)

s = input()

d = {}
for i in range(len(s)):
    d.update({s[i]: s[-i-1]})

print(d)

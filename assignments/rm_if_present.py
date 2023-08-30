s = set({})
s.union("hi", "hello", "bye")

for i in s:
    if i == "hello":
        s.remove("hello")

for i in s:
    print(i)

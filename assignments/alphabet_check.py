s = input("Enter an alphabet: ")
new_s = s[:1]

vowel = ["a", "e", "i", "o", "u"]
for i in vowel:
    if i == new_s:
        print("vowel")
        exit()
else:
    print("consonant")

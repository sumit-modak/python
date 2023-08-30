l = [(169, "sumit"), 
     (167, "sujit"), 
     (166, "sudipta"), 
     (159, "srinjoy"), 
     (154, "souvik")]

# type casting from list to dict
dic = dict(l)
print(dic)

# sorted dictionary
tl = list(dic)
tl.sort()
for i in range(len(l)): 
    temp = (tl[i], dic[tl[i]])
    print(temp)

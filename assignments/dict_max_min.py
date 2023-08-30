d = {169: "sumit", 
     167: "sujit", 
     166: "sudipta", 
     159: "srinjoy", 
     154: "souvik_s",
     150: "souvik_k",
     162: "subhadip"}

l = list(d)
max = -999999999
min =  999999999
for i in l:
    if i < min:
        min = i
    if i > max:
        max = i

print("Max: ",max)
print("Min: ",min)

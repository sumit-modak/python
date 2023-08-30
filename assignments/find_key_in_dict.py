d = {169: "sumit", 
     167: "sujit", 
     166: "sudipta", 
     159: "srinjoy", 
     154: "souvik_s",
     150: "souvik_k",
     162: "subhadip"}

key = int(input("Key: "))
flag = False
l = list(d)
for k in l:
    if k == key:
        flag = True

if flag:
    print("Present")
else:
    print("not Present")
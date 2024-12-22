import os 

for (root,dirs,files) in os.walk('/home/sumit/priv/self'):
    print(root, end="\n\n")
    print(dirs, end="\n\n")
    print(files, end="\n\n")
    print("---------------")

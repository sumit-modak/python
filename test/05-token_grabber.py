import os
import re

# path = "/home/sumit/alt/python/test/lol"
path = "/home/sumit/.config/BraveSoftware/Brave-Browser/Profile 2/Local Storage/leveldb"
for file in os.listdir(path):
    if file.endswith(".log") or file.endswith(".ldb")   :
        for line in [x.strip() for x in open(f"{path}/{file}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", r"mfa\.[\w-]{80,95}"):
                for token in re.findall(regex, line):
                    print(token, type(token), "\n")

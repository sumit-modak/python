from urllib.request import Request, urlopen
import os
from json import loads

def getip():
    try:return urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:return "None"

IP = getip()

def globalinfo():
    try:
        username = os.getenv("USER")
        ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{IP}")).read().decode().replace('callback(', '').replace('})', '}')
        ipdata = loads(ipdatanojson)
        contry = ipdata["country_name"]
        contryCode = ipdata["country_code"].lower()
        if contryCode == "not found":
            globalinfo = f":rainbow_flag:  - `{username.upper()} | {IP} ({contry})`"
        else:
            globalinfo = f":flag_{contryCode}:  - `{username.upper()} | {IP} ({contry})`"
        return globalinfo

    except:
        return f":rainbow_flag:  - `{username.upper()}`"


print(globalinfo())

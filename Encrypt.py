import cryptography
from cryptography.fernet import Fernet

#key = Fernet.generate_key()

#Write key
'''
file = open('key.key', 'wb')
file.write(key) # The key is type bytes still
file.close()
'''
#Open Key
file = open('key.key', 'rb')
key = file.read() # The key will be type bytes
file.close()

#Open Pass
p = open("Pass.txt","r")
pw = p.read()
pw = pw.encode()

f = Fernet(key)
encrypted = f.encrypt(pw)

p.close()


#Write pass enconded
f = open("Pass.txt","wb")
f.write(encrypted)
f.close()
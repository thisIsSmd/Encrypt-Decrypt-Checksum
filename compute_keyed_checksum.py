import hmac
import hashlib

with open ('key.bin', 'rb') as f:
    HMAC_SHA_KEY = f.read()

print(HMAC_SHA_KEY)

path = input("Enter the location of the file to calculate the hash\n") 
with open (path, 'rb') as f:
    textData = f.read()

print(textData)

hashCode = hmac.new(HMAC_SHA_KEY, textData, hashlib.sha256 ).hexdigest()

print(hashCode)

with open ('sensitive_keyed_checksum.txt', 'wb') as f:
    f.write(hashCode.encode())
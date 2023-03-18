import hashlib

path = input("Enter the location of the file to calculate the SHA256\n")

with open(path, 'rb') as f:
    dataContent = f.read()

codeHash = hashlib.sha256(dataContent).hexdigest()

with open('sensitive_checksum.txt','wb') as f:
    f.write(codeHash.encode())

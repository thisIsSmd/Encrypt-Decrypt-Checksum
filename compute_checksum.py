import hashlib

path = input("Enter the location of the file to calculate the SHA256\n")

with open(path, 'rb') as f:
    dataContent = f.read()

codeHash = hashlib.sha256(dataContent).hexdigest()

with open('sensitive_checksum.txt','wb') as f:
    f.write(codeHash.encode())

#5. verify_checksum.py

import hashlib

path = input("Enter the location of the Sensitive file hash\n")
fileWithHashLoc = input("Enter the location of the file to verify the hash\n")

with open(path, 'rb') as f:
    OrgFile = f.read().decode()
    

with open(fileWithHashLoc, 'rb') as f:
    verifyHashContents = f.read()

hashCode = hashlib.sha256(verifyHashContents).hexdigest()

if ( OrgFile == hashCode ):
    print("Accept")
else:
    print ("Reject")

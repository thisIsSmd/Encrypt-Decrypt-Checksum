import hmac
import hashlib

with open ('key.bin', 'rb') as f:
    HMAC_KEY = f.read()

path = input("Enter the location of the original hash file\n")
verifyHashLoc = input("Enter the location of the file to verify the hash\n") 


with open (path, 'rb') as f:
    OrgFileHash = f.read().decode()

#print(orig_file_hash)

with open (verifyHashLoc, 'rb') as f:
    verifyContents = f.read()

hashCode = hmac.new(HMAC_KEY, verifyContents, hashlib.sha256 ).hexdigest()

#print(hashcode)

if ( OrgFileHash == hashCode):
    print("Accept")
else:
    print ("Reject")

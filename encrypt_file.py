import rsa

with open ('pub_key.pem','rb') as f:
    Public_Key = rsa.PublicKey.load_pkcs1(f.read())
    pkey = f.read()


path = input("Enter the location of the file that needs to be encrypted\n")
 
with open (path, 'rb') as fi:
    textData = fi.read()


cipherText = []
for i in range(0, len(textData), 373):
    chunk = textData[i:i+373]
    cipherText.append(rsa.encrypt(chunk, Public_Key))

Cyber_bytes = b''.join(cipherText)


with open ('encryptedFile.txt','wb') as f:
    f.write(Cyber_bytes)
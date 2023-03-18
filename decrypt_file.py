import rsa

with open ('priv_key.pem','rb') as f:
    priv_key = rsa.PrivateKey.load_pkcs1(f.read())
    pkey = f.read()


path = input("Enter the location of the file that needs to be decrypted\n")

with open (path, 'rb') as f:
    cipherText = f.read()

plainText = []
for i in range(0, len(cipherText), 384):
    chunk = cipherText[i:i+384]
    plainText.append(rsa.decrypt(chunk, priv_key).decode())

plainbyte = ''.join(plainText)


with open ('decryptedFile.txt','wb') as f:
    f.write(plainbyte.encode())
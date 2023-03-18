import rsa

(Public_Key, Private_Key) = rsa.newkeys(3072) #3072 Bit

with open('pub_key.pem', 'wb') as f: #Saving it in the pub_key file
    f.write(Public_Key.save_pkcs1('PEM')) 

with open('priv_key.pem', 'wb') as f: #Saving it in the priv_key file
    f.write(Private_Key.save_pkcs1('PEM'))

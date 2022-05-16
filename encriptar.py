import fernet
import rsa
'''#r=crypto.Random.new().read
(pubkey,privkey)=rsa.newkeys(1024)
message=b'mysecret'
crypto=rsa.encrypt(message,pubkey)
decr=rsa.decrypt(crypto,privkey)
print(decr.decode())'''

#abrir el archivo con la llave simetrica
#skey=open('symmetric.key','rb')
#key=skey.read()
#creando el cifrado
#cipher=fernet.Fernet(key)

#abriendo el archivo a cifrar
myfile=open('archivo.txt','rb')
myfiledata=myfile.read()

#encriptar archivo
#encrypted_data=cipher.encrypt(myfiledata)
#edata=open('archivoencriptado','wb')
#edata.write(encrypted_data)

#print(encrypted_data)

#abrir llave publica
pkey=open('publickey.key','rb')
pkdata=pkey.read()

#cargar la llave
pubkey=rsa.PublicKey.load_pkcs1(pkdata)

#encriptando el archivo con la llave simetrica
encrypted_file=rsa.encrypt(myfiledata,pubkey)

ekey=open('encrypted_file','wb')
ekey.write(encrypted_file)

print(encrypted_file)
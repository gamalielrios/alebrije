import fernet
import rsa
import base64
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
#abrir el archivo a encriptar en modo lectura binaria
myfile=open('3er.JPG','rb')
myfiledata=myfile.read()
print(myfiledata)
myfile2=open('img.txt','rb')
myfiledata2=myfile2.read()
convert_img= base64.b64encode(myfiledata)
imgb64=open('img_b64.bin','wb')
imgb64.write(convert_img)

print(imgb64)
#encriptar archivo
#encrypted_data=cipher.encrypt(myfiledata)
#edata=open('archivoencriptado','wb')
#edata.write(encrypted_data)

#print(encrypted_data)

#abrir llave publica
#abrir la llave publica para cifrar en modo lectura binaria
pkey=open('publickey.key','rb')
pkdata=pkey.read()

#cargar la llave
pubkey=rsa.PublicKey.load_pkcs1(pkdata)

#encriptando el archivo con la llave publica
encrypted_file=rsa.encrypt(myfiledata2,pubkey)

#creando el archivo encriptado
ekey=open('img_encriptad45','wb')
ekey.write(encrypted_file)
#print(encrypted_file)
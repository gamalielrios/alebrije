import fernet
import rsa

prkey=open('privkey.key','rb')
prkdata=prkey.read()

#cargar la llave
private_key=rsa.PrivateKey.load_pkcs1(prkdata)

efile=open('encrypted_file','rb')
encrypted_file=efile.read()

decrypted=rsa.decrypt(encrypted_file,private_key)

print(decrypted)
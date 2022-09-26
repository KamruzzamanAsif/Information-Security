from AES_Funcitons import *

fin = open("/home/asif/Information-Security/LabFinal/FileEncryptDecrypt/input.txt", "r")
text = fin.readline()
key = fin.readline()

fout = open("/home/asif/Information-Security/LabFinal/FileEncryptDecrypt/output.txt", "w+")
cipher_text = Encrypt(text, key)
fout.write(cipher_text+'\n')
plain_text = Decrypt(cipher_text, key)
plain_text = plain_text[:len(text)]
fout.write(plain_text)




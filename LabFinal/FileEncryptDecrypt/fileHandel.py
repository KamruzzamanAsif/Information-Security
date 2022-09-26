from AES_Funcitons import *

fin = open("/home/asif/Information-Security/LabFinal/FileEncryptDecrypt/input.txt", "r")
text = fin.readline()
key = fin.readline()

fout = open("/home/asif/Information-Security/LabFinal/FileEncryptDecrypt/output.txt", "w+")
cipher_text = Encrypt(text, key)
fout.writelines(cipher_text)
plain_text = Decrypt(cipher_text, key)
fout.writelines(plain_text)




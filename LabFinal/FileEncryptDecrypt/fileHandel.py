from AES_Funcitons import *

fin = open("/home/asif/Information-Security/LabFinal/FileEncryptDecrypt/input.txt", "r")
temp = fin.read().splitlines()
text = temp[0]
key = temp[1]

fout = open("/home/asif/Information-Security/LabFinal/FileEncryptDecrypt/output.txt", "w+")
cipher_text = Encrypt(text, key)
fout.write(cipher_text+'\n')
plain_text = Decrypt(cipher_text, key)
plain_text = plain_text[:len(text)]
fout.write(plain_text)




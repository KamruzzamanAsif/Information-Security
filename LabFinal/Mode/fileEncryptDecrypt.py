# from AES_CBC import *
# from AES_CTR import *
import AES_CBC
import AES_CTR

print("Choose Encryption Mode: \n 1. AES_CBC \t 2. AES_CTR")
i = int(input())

if i == 1:
    f = open("/home/asif/Information-Security/LabFinal/Mode/CBCinput.txt", "r")
    temp = f.read().splitlines()
    text = temp[0]
    key = temp[1]
    iv = temp[2]
    f.close()
    cipher = AES_CBC.Encrypt(text, key, iv)
    fout = open("/home/asif/Information-Security/LabFinal/Mode/CBCoutput.txt", "w+")
    fout.write(cipher)
    fout.close()

elif i == 2:
    f = open("/home/asif/Information-Security/LabFinal/Mode/CTRinput.txt", "r")
    temp = f.read().splitlines()
    text = temp[0]
    key = temp[1]
    counter = temp[2]
    cipher = AES_CTR.Encrypt(text, key, counter)
    fout = open("/home/asif/Information-Security/LabFinal/Mode/CTRoutput.txt", "w+")
    fout.write(cipher)

else:
    print("Invalid mode")
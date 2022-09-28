import AES_CTR

print(">>>>>>>Welcome to AES_CTR-128bit Encryption Decryption<<<<<<<<")
print("[Note:  1. text is taken form input.txt file\n\t2. cipher is stored in output1.txt file\n\t3. decrypted plain text is stored in output2.txt file]")
print()

f = open("BSSE 1217/input.txt", "r")
text = f.read()
f.close()

print("Enter a 16 byte key as string: ", end=" ")
key = input()
if(len(key)!=16):
    print("Invalid key")

print("Enter a 16 byte counter as string: ", end=" ")
counter = input()
if(len(counter)!=16):
    print("Invalid counter")

cipher = AES_CTR.Encrypt(text, key, counter)
fout1 = open("BSSE 1217/output1.txt", "w+")
fout1.write(cipher)
fout1.close()

print("Encryption Done!")

plainText = AES_CTR.Decrypt(cipher, key, counter)
fout2 = open("BSSE 1217/output2.txt", "w+")
fout2.write(plainText)
fout2.close()

print("Decryption Done!")

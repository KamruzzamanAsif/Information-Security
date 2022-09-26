from SHA_Funcitons import *
from AES_Funcitons import *

# make message digest
fin = open("/home/asif/Information-Security/LabFinal/DigitalSignature/signature.txt", "r")
text = fin.read()
fin.close()

message_digest = SHA512(text)
fout = open("/home/asif/Information-Security/LabFinal/DigitalSignature/messageDigest.txt", "w+")
fout.writelines(message_digest)
fout.close()

# encrypt message digest
ffin = open("/home/asif/Information-Security/LabFinal/DigitalSignature/messageDigest.txt", "r")
md = ffin.readline()
digest = "0x" + md # in our sha output 0x was not included
ffin.close()

fkey = open("/home/asif/Information-Security/LabFinal/DigitalSignature/senderPrivateKey.txt", "r")
sender_private_key = fkey.read()
digital_signature = Encrypt(digest, sender_private_key)
fkey.close()

fdgs = open("/home/asif/Information-Security/LabFinal/DigitalSignature/digitalSignature.txt", "w+")
fdgs.write(digital_signature)
fdgs.close()

# receiver validate
sender_public_key = sender_private_key   # as we are using symmetric encryption here

calculated_message_digest = Decrypt(digital_signature, sender_public_key)
print(digest)
print(calculated_message_digest[ :len(digest)])
if calculated_message_digest[ :len(digest)] == digest:  # as we padd in encryption so we will take
    print("Yes validated!")                             # just up to digest length
    


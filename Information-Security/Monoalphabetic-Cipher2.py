def encryption(plain_text):
    cipher = ''
 
    for letter in plain_text:
        if(letter != ' '):
            a = ord(letter)+5
            cipher += chr(a)
        else:
            cipher += ' '

    return cipher


def decryption(cipher):
    plain_text = ''
    
    for letter in cipher:
        if(letter != ' '):
            a = ord(letter)-5
            plain_text += chr(a)
        else:
            plain_text += ' '
    
    return plain_text


def main():
    # text = "Cryptography is fun"
    text = input()
    cipher = encryption(text)
    print("Encrypted message (cipher text):")
    print(cipher)
    
    print("Decypted message (plain text):")
    print(decryption(cipher))


if __name__ == '__main__':
    main()

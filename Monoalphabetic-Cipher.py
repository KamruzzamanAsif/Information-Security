monoalphabetic_table = {
        'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 
        'Z' : 'A',
        'a' : 'z', 'b' : 'y', 'c' : 'x', 'd' : 'w', 'e' : 'v',
        'f' : 'u', 'g' : 't', 'h' : 's', 'i' : 'r', 'j' : 'q',
        'k' : 'p', 'l' : 'o', 'm' : 'n', 'n' : 'm', 'o' : 'l',
        'p' : 'k', 'q' : 'j', 'r' : 'i', 's' : 'h', 't' : 'g',
        'u' : 'f', 'v' : 'e', 'w' : 'd', 'x' : 'c', 'y' : 'b', 
        'z' : 'a'}

def encryption(plain_text):
    cipher = ''
 
    for letter in plain_text:
        if(letter != ' '):
            cipher += monoalphabetic_table[letter]
        else:
            cipher += ' '

    return cipher


def decryption(cipher):
    plain_text = ''
    
    for letter in cipher:
        if(letter != ' '):
            plain_text += monoalphabetic_table[letter]
        else:
            plain_text += ' '
    
    return plain_text


def main():
    text = "Cryptography is fun"
    cipher = encryption(text)
    print("Encrypted message (cipher text):")
    print(cipher)
    
    print("Decypted message (plain text):")
    print(decryption(cipher))


if __name__ == '__main__':
    main()

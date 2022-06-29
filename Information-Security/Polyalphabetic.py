from pydoc import plain
from time import process_time_ns


def make_table(row, column):
    polyalphabetic_table = [["" for i in range(column)]for j in range(row)]
    
    for i in range(row):
        for j in range(column):
            a = (i + j - 30) % column   # my defined funciton
            polyalphabetic_table[i][j] = chr(a)
    
    return polyalphabetic_table

def encryption(plain_text, polyalphabetic_table):
    cipher = ''
    for i in range(len(plain_text)):
        if(plain_text[i] != ' '):
            index = int(ord(plain_text[i])- 0x00)  # ascii value of NULL is 0x00
            length = i%128
            cipher += polyalphabetic_table[index][length]
        else:
            cipher += ' '
            
    return cipher


def decryption(cipher, polyalphabetic_table, row, coloumn):
    plain_text = ''
    for i in range(len(cipher)):
        if(cipher[i] != ' '):
            x = cipher[i]
            x_pos = i % 128
            for j in range(row):
                if(polyalphabetic_table[j][x_pos] == x):
                    a = j + 0x00
                    plain_text += chr(a)    
        else:
            plain_text += ' '
            
    return plain_text

def main():
    row = 128
    coloumn = 128
    polyalphabetic_table = make_table(row, coloumn)
    
    plain_text = "Cryptography is Fun and Love" 
    cipher = encryption(plain_text, polyalphabetic_table)
    print("Encrypted message (cipher text):")
    print(cipher)

    print("Decypted message (plain text):")
    print(decryption(cipher, polyalphabetic_table, row, coloumn))


    
if __name__ == '__main__':
    main()
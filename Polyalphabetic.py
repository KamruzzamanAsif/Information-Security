from pydoc import plain
from time import process_time_ns


def make_table(row, column):
    polyalphabetic_table = [["" for i in range(column)]for j in range(row)]
    
    for i in range(row):
        for j in range(column):
            a = (i + ord('a') + j - 30) # my defined funciton
            polyalphabetic_table[i][j] = chr(a)
    
    return polyalphabetic_table

def encryption(plain_text, polyalphabetic_table):
    cipher = ''
    for i in range(len(plain_text)):
        if(plain_text[i] != ' '):
            index = int(ord(plain_text[i])- ord('a'))
            length = i%25
            cipher += polyalphabetic_table[index][length]
        else:
            cipher += ' '
            
    return cipher


def decryption(cipher, polyalphabetic_table, row, coloumn):
    plain_text = ''
    for i in range(len(cipher)):
        if(cipher[i] != ' '):
            x = cipher[i]
            x_pos = i % 25
            for j in range(row):
                if(polyalphabetic_table[j][x_pos] == x):
                    a = j + ord('a')
                    plain_text += chr(a)    
        else:
            plain_text += ' '
            
    return plain_text

def main():
    row = 26
    coloumn = 25
    polyalphabetic_table = make_table(26, 25)
    for i in range(len(polyalphabetic_table)):
        for j in range(len(polyalphabetic_table[i])):
            print(polyalphabetic_table[i][j], end=" ")
        print()
    
    plain_text = "java is love and python is guru"
    cipher = encryption(plain_text, polyalphabetic_table)
    print("Encrypted message (cipher text):")
    print(cipher)

    print("Decypted message (plain text):")
    print(decryption(cipher, polyalphabetic_table, row, coloumn))


    
if __name__ == '__main__':
    main()
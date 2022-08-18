#######################################################
#       This is a pure AES program to                 #
#       Encrypt and Decrypt a cipher text             #
#       @Owner: Kamruzzaman Asif                      #
#       Undergraduate student at IIT, DU              #
#       Date: 16 August 2022                          #
#######################################################


import re


Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)


Rcon = (
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
    0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
)


def string_to_hex_converter(string):
    ################################################################
    #       sample input : hello  (string)                         #
    #       sample output: 448378203247 (0x68656c6c6f in hexa)     #
    # ***>> Because there is no such int hex object in python      #
    #       hex() function just returns the string representation  #
    #       of your hex value                                      #
    # ***>> We can return "0x68656c6c6f"                           #
    # ***>> But can't return int hex object like: 0x68656c6c6f     #
    # ***>> That's why for simple calculation purpose we use       #
    #       int representation of hexa and return an int           #
    # $$$$$ for more: https://cutt.ly/KXxFsLJ                      #
    ################################################################
    
    hex_string = ''   # temp hex string to store hex value as one single string
    # for first char
    h = hex(ord(string[0]))
    hex_string += h
    # for other char
    for i in range(1, len(string)):
        h = hex(ord(string[i]))
        hex_string += h[2:]
    
    # now convert the hex string into an integer
    # which is same value in hexadecimal
    hex_value = int(hex_string, 16)
    
    return hex_value



def plainHexValues_to_matrix_converter(hex_value):
    #########################################################################
    #       sample input : hex_value 57811460909138771071931939740208549692 #
    #                      (in hexa 0x2b7e151628aed2a6abf7158809cf4f3c)     #
    #       sample output: [[43, 40, 171, 9],                               #
    #                       [126, 174, 247, 207],                           #
    #                       [21, 210, 21, 79],                              #
    #                       [22, 166, 136, 60]]                             #
    #                     --in hexa:                                        #
    #                       [[0x2b, 0x28, 0xab, 0x9],                       #
    #                       [0x7e, 0xae, 0xf7, 0xcf],                       #
    #                       [0x15, 0xd2, 0x15, 0x4f],                       #
    #                       [0x16, 0xa6, 0x88, 0x3c]]                       #
    #########################################################################
    
    # right shifting the values and bitwise and with ff to get the byte
    # for example if we get 2b7e after right shifting the the and with
    # ff will give output 7e
    """ 
    An example of calculation:
        2b7e in binary = 0010101101111110
        ff in binary   = 0000000011111111
        ----------------------------------
    bitwise and value  = 0000000001111110 = 0x7e
    """

    row, column = (4, 4)
    matrix = [[0x00 for i in range(column)]for j in range(row)] # initalize the matrix with hex 0 value

    index = 0 # for hex_value
    for j in range(4):
        for i in range(4):
            byte = (hex_value >> (8 * (15 - index))) & 0xFF
            matrix[i][j] = byte # storing values column wise
            index = index + 1 # update hex_value index
        
    return matrix



def key_expansion(hex_key):
    #############################################################################
    #    Sample input: hex_value 57811460909138771071931939740208549692         #
    #                      (in hexa 0x2b7e151628aed2a6abf7158809cf4f3c)         #
    #    Sample output:                                                         #
    #           [[43, 126, 21, 22], [40, 174, 210, 166], [171, 247, 21, 136],   #
    #            [9, 207, 79, 60], [160, 251, 255, 22], [136, 85, 45, 176],     #
    #            [35, 162, 56, 56], [42, 109, 119, 4], [158, 12, 15, 241],      #
    #            [22, 89, 34, 65], [53, 251, 26, 121], [31, 150, 109, 125],     #
    #            [10, 52, 244, 53], [28, 109, 214, 116], [41, 150, 204, 13],    #
    #            [54, 0, 161, 112], [97, 14, 173, 56], [125, 99, 123, 76],      #
    #            [84, 245, 183, 65], [98, 245, 22, 49], [151, 89, 122, 130],    #
    #            [234, 58, 1, 206], [190, 207, 182, 143], [220, 58, 160, 190],  #
    #            [55, 153, 244, 36], [221, 163, 245, 234], [99, 108, 67, 101],  #
    #            [191, 86, 227, 219], [198, 200, 13, 108], [27, 107, 248, 134], #
    #            [120, 7, 187, 227], [199, 81, 88, 56], [151, 34, 138, 42],     #
    #            [140, 73, 114, 172], [244, 78, 201, 79], [51, 31, 145, 119],   #
    #            [76, 184, 100, 242], [192, 241, 22, 94], [52, 191, 223, 17],   #
    #            [7, 160, 78, 102], [154, 161, 97, 1], [90, 80, 119, 95],       #
    #            [110, 239, 168, 78], [105, 79, 230, 40]]                       #
    # ###########################################################################
  
    
   key_matrix = plainHexValues_to_matrix_converter(hex_key)
   round_key = [] # to store the round keys
   
   # at first copy the first 16 bytes (4 words) column wise
   # as the key_matrix is formed as column wise
   for j in range(4):
    temp_list = []
    for i in range(4):
        temp_list.append(key_matrix[i][j])
    round_key.append(temp_list)
   
   # now add more keys to round key matrix (total 4 word + 40 word)
   for i in range(4, 44):
       round_key.append([]) # add a new row
       if i%4 == 0:
            # we will first sub byte and xor with index 1 value of round key[i-1] 
            # because Rcon left circular shift by 1 byte
            # doing the below things works for Rcon automatically
            byte = round_key[i-4][0] ^ (Sbox[int(round_key[i-1][1])] ^ Rcon[int(i/4)])
            round_key[i].append(byte)
            
            for j in range(1,4):
                # used % to get the index 0 while j+1 = 4
                byte = round_key[i-4][j] ^ (Sbox[int(round_key[i-1][(j+1)%4])] ^ Rcon[int(i/4)])
                round_key[i].append(byte)
       else:
           for j in range(4):
               byte = round_key[i-4][j] ^ round_key[i-1][j] # w[i] = w[i-4] xor temp -> (w[i-1])
               round_key[i].append(byte)
    
   return round_key


def add_round_key(text_matrix, w_keys):
    for i in range(4):
        for j in range(4):
            text_matrix[i][j] ^= w_keys[i][j] 
    
    return text_matrix
    
def substitute_bytes(text_matrix):
    for i in range(4):
        for j in range(4):
            #print (text_matrix[i][j])
            text_matrix[i][j] = Sbox[int(text_matrix[i][j])] 
    
    return text_matrix

def shift_rows(text_matrix):
    text_matrix[1][0], text_matrix[1][1], text_matrix[1][2], text_matrix[1][3] \
        = text_matrix[1][1], text_matrix[1][2], text_matrix[1][3], text_matrix[1][0]
    text_matrix[2][0], text_matrix[2][1], text_matrix[2][2], text_matrix[2][3] \
        = text_matrix[2][2], text_matrix[2][3], text_matrix[2][0], text_matrix[2][1]
    text_matrix[3][0], text_matrix[3][1], text_matrix[3][2], text_matrix[3][3] \
        = text_matrix[3][3], text_matrix[3][0], text_matrix[3][1], text_matrix[3][2]
    
    return text_matrix


def two_mul(a):
    if(a & 0x80): # check is high bit is 1
        a = ((a << 1) ^ 0x1B) & 0xFF  # bitwise and with FF to set length within 8 bit else
                                      # program will make it 9 bit
                                      # eg. 11001100 << 1   =  110011000 (9 bit as pc calculate on 16 bits)
    else:
        a = a << 1

    return a


def three_mul(a):
    a = two_mul(a) ^ a
    
    return a


def mix_columns(text_matrix):
    s = [[0x00 for i in range(4)]for j in range(4)]
    
    for j in range(4):
        s[0][j] = two_mul(text_matrix[0][j]) ^ three_mul(text_matrix[1][j]) ^ text_matrix[2][j] ^ text_matrix[3][j]
        s[1][j] = text_matrix[0][j] ^ two_mul(text_matrix[1][j]) ^ three_mul(text_matrix[2][j]) ^ text_matrix[3][j]
        s[2][j] = text_matrix[0][j] ^ text_matrix[1][j] ^ two_mul(text_matrix[2][j]) ^ three_mul(text_matrix[3][j])
        s[3][j] = three_mul(text_matrix[0][j]) ^ text_matrix[1][j] ^ text_matrix[2][j] ^ two_mul(text_matrix[3][j])
    
    return s


def matrix_to_hex_converter(matrix):
    #######################################
    #   sample input: matrix of int       #
    #   sample output: hex string         #
    #######################################
    
    text = '0x'
    for j in range(4):
        for i in range(4):
            s = hex(matrix[i][j])
            text += s[2:]
    
    return text


def encryption(hexValue_text, round_key):
    #####################################################
    #       Sample input: plainText (as hex value text) #
    #       Sample output: cihper text(as hex string)   #
    #####################################################
    text_matrix = plainHexValues_to_matrix_converter(hexValue_text)
    
    text_matrix = add_round_key(text_matrix, round_key[:4]) # pass first 4 list(words) from round key
    
    for i in range(1, 10):
        text_matrix = substitute_bytes(text_matrix)
        text_matrix = shift_rows(text_matrix)
        text_matrix = mix_columns(text_matrix)
        text_matrix = add_round_key(text_matrix, round_key[4 * i : 4 * (i + 1)])
    
    text_matrix = substitute_bytes(text_matrix)
    text_matrix = shift_rows(text_matrix)
    text_matrix = add_round_key(text_matrix, round_key[40:])
    
    print("Cipher matrix: ", end=' ')
    print(text_matrix)
    cipher_text = matrix_to_hex_converter(text_matrix)
    
    return cipher_text



def inv_substitute_bytes(matrix):
    for i in range(4):
        for j in range(4):
            matrix[i][j] = InvSbox[matrix[i][j]]
    
    return matrix 

def inv_shift_rows(matrix):
    matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3] = \
        matrix[1][3], matrix[1][0], matrix[1][1], matrix[1][2]
        
    matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3] = \
        matrix[2][2], matrix[2][3], matrix[2][0], matrix[2][1]
        
    matrix[3][0], matrix[3][1], matrix[3][2], matrix[3][3] = \
        matrix[3][1], matrix[3][2], matrix[3][3], matrix[3][0]
    
    return matrix
    

def inv_mix_columns(matrix):
    
    # what to do...?



def decryption(cipherText_value, round_key):
    cipher_state_matrix = plainHexValues_to_matrix_converter(cipherText_value)
    
    cipher_state_matrix = add_round_key(cipher_state_matrix, round_key[40: ])
    cipher_state_matrix = inv_shift_rows(cipher_state_matrix)
    cipher_state_matrix = inv_substitute_bytes(cipher_state_matrix)
    
    for i in range(9, 0, -1):
        cipher_state_matrix = add_round_key(cipher_state_matrix, round_key[4 * i : 4 * (i + 1)])
        cipher_state_matrix = inv_mix_columns(cipher_state_matrix)
        cipher_state_matrix = inv_shift_rows(cipher_state_matrix)
        cipher_state_matrix = inv_substitute_bytes(cipher_state_matrix)
    
    cipher_state_matrix = add_round_key(cipher_state_matrix, round_key[:4])
    
    plain_hex = matrix_to_hex_converter(cipher_state_matrix)
    
    return plain_hex


def main():
    # # input a text block
    # while True:
    #     print("Enter a text block to encrypt or decrypt: ",end=" ")
    #     text = input()
    #     if len(text) != 16:
    #         print("Invalid text block input!")
    #     else:
    #         break
    
    # # input a key
    # while True:
    #     print("Enter a key: ",end=" ")
    #     key = input()
    #     if len(key) != 16:
    #         print("Invalid key input!")
    #     else:
    #         break
    
    text = "Two One Nine Two"
    key = 'Thats my Kung Fu'  # expansion key mile na...(kavaliro.com er pdf er sathe) baki sob thik ace
    
    
    # taking the hex values as we will work with hex values
    hexValue_text = string_to_hex_converter(text)
    hexValue_key = string_to_hex_converter(key)
    
    # round key formation
    round_key = key_expansion(hexValue_key)
    
    # encryption
    cipher_text= encryption(hexValue_text, round_key)
    print("cipher text: " + cipher_text)
    
    # decryption
    cipherText_value = int(cipher_text, 16)
    plain_text_hex = decryption(cipherText_value, round_key)
    
    
    
if __name__ == '__main__':
    main()
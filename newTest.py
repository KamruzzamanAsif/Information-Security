
def two_mul(a):
    if(a & 0x80): # check is high bit is 1
        a = ((a << 1) ^ 0x1B) & 0xFF  # bitwise and with FF to set length within 8 bit else
                                      # program will make it 9 bit
                                      # eg. 11001100 << 1   =  110011000 (9 bit as pc calculate on 16 bits)
    else:
        a = a << 1

    return a


def E_mul(x):
    # hex E in decimal 14
    a = two_mul((two_mul((two_mul(x) ^ x)) ^ x))
    
    return a 

def B_mul(x):
    # hex B in decimal 11
    a = two_mul((two_mul(two_mul(x)) ^ x)) ^ x
    
    return a 

def D_mul(x):
    # hex D in decimal 13
    a = two_mul(two_mul(two_mul(x) ^ x)) ^ x 
    
    return a

def nine_mul(x):
    a = two_mul(two_mul(two_mul(x))) ^ x
    
    return a

def inv_mix_columns(matrix):
    s = [[0x00 for i in range(4)]for j in range(4)]
    
    for j in range(4):
        s[0][j] = E_mul(matrix[0][j]) ^ B_mul(matrix[1][j]) ^ D_mul(matrix[2][j]) ^ nine_mul(matrix[3][j])
        s[1][j] = nine_mul(matrix[0][j]) ^ E_mul(matrix[1][j]) ^ B_mul(matrix[2][j]) ^ D_mul(matrix[3][j])
        s[2][j] = D_mul(matrix[0][j]) ^ nine_mul(matrix[1][j]) ^ E_mul(matrix[2][j]) ^ B_mul(matrix[3][j])
        s[3][j] = B_mul(matrix[0][j]) ^ D_mul(matrix[1][j]) ^ nine_mul(matrix[2][j]) ^ E_mul(matrix[3][j])
    
    for i in range(4):
        for j in range(4):
            print(hex(s[i][j]), end=" ")
        print()

m = [[0x47, 0x40, 0xa3, 0x4c], [0x37, 0xd4, 0x70, 0x9f], [0x94, 0xe4, 0x3a, 0x42], [0xed, 0xa5, 0xa6, 0xbc]]

inv_mix_columns(m)

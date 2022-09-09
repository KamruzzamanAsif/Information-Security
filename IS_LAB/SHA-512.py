#######################################################
#       SHA-512 implementation                        #
#       @Owner: Kamruzzaman Asif                      #
#       Undergraduate student at IIT, DU              #
#       Date: 08 September 2022                       #
#######################################################

def stringToBinary(string):
    """
    Convert a string to a binary string.
    :param string: String to convert.
    :return: Binary string.
    """
    return ' '.join('{0:08b}'.format(ord(x), 'b') for x in string)


def intToBinary(x, y):
    """
    Convert an integer to a binary string.
    :param x: Integer to convert.
    :param y: x is a y-bit integer.
    :return: Binary string of y bit.
    """
    if y == 128: return "{0:0128b}".format(x) # for length binary data
    if y == 64: return "{0:064b}".format(x) # for W data


def preprocess(string1, string2):
    """
    Preprocess a string.
    :param string1: binary string to preprocess.
    :param string2: binary string to preprocess.
    :return: final preprocessed binary string for SHA-512.
    """
    l = int((len(string1)+len(string2)) % 1024)
    if l == 0: return string1 + string2
    else: return string1 + '1' + format(0, 'b').zfill(1023-l) + string2


def additionModulo(string1, string2):
    """Addition of two strings values
     : param string1: the first string
     : param string2: the second string
     : return additionModulo of string1 and string2 to 2^64
        as string value
    """ 
    x = int(string1, 2)
    y = int(string2, 2)

    return intToBinary(int((x+y) % (2**64)), 64) 

def xor(x, y):
    s = ''
    for i in range(len(x)): 
        if x[i] == y[i]: s += '0'
        else: s += '1'
    return s

def ROTR(x, n): return x[len(x)-n: ] + x[ :len(x)-n]
def SHR(x, n): return x[n: ].ljust(64, '0')  # ljust funciton for padding 0 to right side

def sigma0(s): return xor(xor(ROTR(s, 1), ROTR(s, 8)), SHR(s, 7))
def sigma1(s): return xor(xor(ROTR(s, 19), ROTR(s, 61)), SHR(s, 6)) 


###################### hash buffers #################################
a = "0110101000001001111001100110011111110011101111001100100100001000"
b = "1011101101100111101011101000010110000100110010101010011100111011"
c = "0011110001101110111100110111001011111110100101001111100000101011"
d = "1010010101001111111101010011101001011111000111010011011011110001"
e = "0101000100001110010100100111111110101101111001101000001011010001"
f = "1001101100000101011010001000110000101011001111100110110000011111"
g = "0001111110000011110110011010101111111011010000011011110101101011"
h = "0101101111100000110011010001100100010011011111100010000101111001"

H = a + b + c + d + e + f + g + h


###################### main Function Body ##################################

def main():
    print("Enter your text: ", end="")
    plalin_text = input()
    text_binary_data = stringToBinary(plalin_text)
    text_binary_data = text_binary_data.replace(' ', '')

    # append length
    length_of_data = len(text_binary_data)
    length_binary_data = intToBinary(length_of_data, 128)

    final_binary_data = preprocess(text_binary_data, length_binary_data)
    print("The final data passed to SHA-512: " + final_binary_data)
    N = int(len(final_binary_data)/1024)
    
    ########## message digest generation begins ###########
    for i in range(N):
        M = ''
        M = final_binary_data[i*1024 : (i+1)*1024]

        ##### words generation for 80 rounds #####
        W = []
        for j in range(16):
            W.append(M[j*64 : (j+1)*64])
        for j in range(16, 80):
            s = ''
            s += additionModulo(sigma1(W[j-2]), sigma0(W[j-15]))
            s = additionModulo(s, W[j-7])
            s = additionModulo(s, W[j-16])
            W.append(s)
        
        ##### rounds #####
        








if __name__ == '__main__':
    main()
    

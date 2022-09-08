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
    return "{0:0128b}".format(x)


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

    print(final_binary_data)
    print(len(final_binary_data))





if __name__ == '__main__':
    main()
    

row, column = (4, 4)
matrix = [[0x00 for i in range(column)]for j in range(row)]
hex_value = 0x2b7e151628aed2a6abf7158809cf4f3c 
index = 0

for j in range(4):
    for i in range(4):
        byte = hex((hex_value >> (8 * (15 - index))) & 0xFF)
        matrix[i][j] = byte # storing values column wise
        index = index + 1 # update index

print(matrix)
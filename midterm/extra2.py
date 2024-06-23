C1 = [0xe9, 0x3a, 0xe9, 0xc5, 0xfc, 0x73, 0x55, 0xd5]
C2 = [0xf4, 0x3a, 0xfe, 0xc7, 0xe1, 0x68, 0x4a, 0xdf]

# perform XOR to M1 and M2
M1_XOR_M2 = []
for num1, num2 in zip(C1, C2):
    M1_XOR_M2.append(num1 ^ num2)

with open('C:/Users/Microsoft/Desktop/midterm/dictionary.txt', 'r') as words_file:
    words = words_file.read().split()
    words = set([word for word in words if len(word) == len(M1_XOR_M2)])
    
    # Try to use M1 in dictionary to find M2 which is valid.
    for word1 in words:
        M1 = [ord(x) for x in word1]
        M2 = [x ^ y for x, y in zip(M1, M1_XOR_M2)]
        word2 = ''.join([chr(x) for x in M2])
        
        if word2 in words:
            pad = [x ^ y for x, y in zip(M1, C1)]
            print('word1 = %s, word2 = %s, pad = %s' % (word1, word2, pad))

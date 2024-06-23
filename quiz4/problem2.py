def lfsr_8bit(state, plaintext_length):
    key = ""
    length = 0

    while length < plaintext_length:
        key += state[0]

        significant_bit = state[0]
        if(significant_bit != state[4]):
            num1 = '1'
        else:
            num1 = '0' 

        if(significant_bit != state[5]):
            num2 = '1'
        else:
            num2 = '0'

        if(significant_bit != state[6]):
            num3 = '1'
        else:
            num3 = '0'
        state = state[1:4] + num1 + num2 + num3 + state[7] + significant_bit

        length += 1
    
    return key

def text_to_binary(text):
    binary_text = ""
    for char in text:
        binary_char = format(ord(char), '08b')  # Convert character to 8-bit binary
        binary_text += binary_char
    return binary_text

def binary_to_text(binary_string):
    text = ""
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        decimal_value = int(byte, 2)
        text += chr(decimal_value)
    return text

def encrypt(key, plaintext):
    ciphertext = ""
    for i in range(len(plaintext)):
        key_bit = int(key[i])
        plaintext_bit = int(plaintext[i])
        encrypted_bit = key_bit ^ plaintext_bit
        ciphertext += str(encrypted_bit)
    return ciphertext

def decrypt(key, ciphertext):
    plaintext = ""
    for i in range(len(ciphertext)):
        key_bit = int(key[i])
        ciphertext_bit = int(ciphertext[i])
        encrypted_bit = key_bit ^ ciphertext_bit
        plaintext += str(encrypted_bit)
    return plaintext


initial_state = "00000001"

plaintext_origin = "ATNYCUWEARESTRIVINGTOBEAGREATUNIVERSITYTHATTRAN\
SCENDSDISCIPLINARYDIVIDESTOSOLVETHEINCREASINGLYCO\
MPLEXPROBLEMSTHATTHEWORLDFACESWEWILLCONTINUET\
OBEGUIDEDBYTHEIDEATHATWECANACHIEVESOMETHINGMU\
CHGREATERTOGETHERTHANWECANINDIVIDUALLYAFTERALLT\
HATWASTHEIDEATHATLEDTOTHECREATIONOFOURUNIVERSI\
TYINTHEFIRSTPLACE"
plaintext_binary = text_to_binary(plaintext_origin)

key = lfsr_8bit(initial_state, len(plaintext_binary))
print(f"key: {key} \n")

ciphertext_binary = encrypt(key, plaintext_binary)
ciphertext = binary_to_text(ciphertext_binary)
print(f"cipertext_binary:\n{ciphertext_binary}\n")
print(f"cipertext:\n{ciphertext}\n")
plaintext_binary = decrypt(key, ciphertext_binary)
plaintext = binary_to_text(plaintext_binary)
print(f"plaintext_binary:\n{plaintext_binary}\n")
print(f"plaintext:\n{plaintext}")

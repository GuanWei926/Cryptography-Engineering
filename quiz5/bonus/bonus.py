import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def generate_random_bytes(num_bytes):
    return bytes(random.randint(0, 255) for _ in range(num_bytes))

def pad(data):
    # Add PKCS7 padding to the data
    padding_length = AES.block_size - (len(data) % AES.block_size)
    padding = bytes([padding_length]) * padding_length
    return data + padding

def encrypt_AES_CBC(data, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(data))
    return iv + encrypted_data

def main():
    num_bytes = 1024*1024
    random_bytes = generate_random_bytes(num_bytes)

    # Write random bytes to a file
    with open("random_bonus.bin", "wb") as f:
        f.write(random_bytes)
    print("Non-cryptographically secure random bytes written to 'random_bonus.bin'.")

    key = get_random_bytes(16)  # Generate a 128-bit key
    encrypted_data = encrypt_AES_CBC(random_bytes, key)
    
    # Write hashed bytes to a file
    with open("random_bonus_AES.bin", "wb") as f:
        f.write(encrypted_data)
    print("Cryptographically secure random bytes encrypted and written to 'random_bonus_AES.bin'.")

if __name__ == "__main__":
    main()

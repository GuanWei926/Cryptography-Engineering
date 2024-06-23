import secrets

def generate_random_bytes(num_bytes):
    return bytes([secrets.randbits(8) for _ in range(num_bytes)])

def main():
    num_bytes = 1024 * 1024  # 1 million bytes
    random_bytes = generate_random_bytes(num_bytes)
    
    # Write random bytes to a file
    with open("random.bin", "wb") as f:
        f.write(random_bytes)
    
    print("Random bytes generated successfully.")

if __name__ == "__main__":
    main()

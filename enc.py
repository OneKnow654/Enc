import argparse
import os
import secrets

def xor_encrypt_decrypt(data: bytes, key: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(data, key))

def read_key(key: str) -> bytes:
    if os.path.isfile(key):
        with open(key, 'rb') as f:
            return f.read()
            
    else:
        return key.encode()

def generate_key():
    # Generate a random key
    key = secrets.token_bytes(8)  # 16 bytes = 128 bits
    return key

def generate_key_save():
    with open("secret.key", "w") as p:
        key = generate_key()
        print(f"The key is used : {key.hex()}")
        p.write(key.hex())
    return "Key has been stored"



def encrypt_file(file_path: str, key: bytes):
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as f:
            data = f.read()

        long_key = (key * (len(data) // len(key) + 1))[:len(data)]

        encrypted_data = xor_encrypt_decrypt(data, long_key)

        encrypted_folder = "encrypted"
        os.makedirs(encrypted_folder, exist_ok=True)

        output_path = os.path.join(encrypted_folder, os.path.basename(file_path) + ".enc")

        with open(output_path, 'wb') as f:
            f.write(encrypted_data)

        print(f"File '{file_path}' encrypted successfully to '{output_path}'.")
    else:
        print("No file found")

def decrypt_file(file_path: str, key: bytes):
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()

        long_key = (key * (len(encrypted_data) // len(key) + 1))[:len(encrypted_data)]

        decrypted_data = xor_encrypt_decrypt(encrypted_data, long_key)
        
        decrypted_folder = "decrypted"
        os.makedirs(decrypted_folder, exist_ok=True)

        # Define the output path within the 'decrypted' folder
        output_path = os.path.join(decrypted_folder, os.path.basename(file_path)[:-4])  # Remove the ".enc" extension
        if output_path.endswith(".enc"):
            output_path = output_path[:-4]

        with open(output_path, 'wb') as f:
            f.write(decrypted_data)

        print(f"File '{file_path}' decrypted successfully to '{output_path}'.")
    else:
        print("No file found")


def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt files using a custom XOR cipher.")
    parser.add_argument("-e", "--encrypt", action="store_const", const="encrypt", dest="action", help="Encrypt the file")
    parser.add_argument("-d", "--decrypt", action="store_const", const="decrypt", dest="action", help="Decrypt the file")
    parser.add_argument("-g", "--generate-key", action="store_true", help="Generate and print a new encryption key")
    parser.add_argument("-gs", "--generate-save", action="store_true", help="Generate and save a new encryption key")
    parser.add_argument("-k", "--key", nargs="?", help="Encryption key")
    parser.add_argument("-K", "--key-file", nargs="?", help="Path to key file")
    parser.add_argument("files", nargs="*", help="Paths to the files to encrypt or decrypt")

    args = parser.parse_args()

    if args.generate_key:
        key = generate_key()
        print("Generated key:", key.hex())
    elif args.generate_save:
        print(generate_key_save())
    elif args.action in ["encrypt", "decrypt"]:
        if not args.key and not args.key_file:
            print("Error: Either a key (-k) or a key file (-K) is required for encryption/decryption.")
            return

        key = read_key(args.key if args.key else args.key_file)
        
        for file_path in args.files:
            if args.action == "encrypt":
                encrypt_file(file_path, key)
            elif args.action == "decrypt":
                decrypt_file(file_path, key)
    else:
        print("No valid action specified. Use -e to encrypt or -d to decrypt.")

if __name__ == "__main__":
    main()

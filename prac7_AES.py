from Crypto.Cipher import AES
import base64

def main():
    print("Choose an option:")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = int(input())
    key = input("Enter the AES key (16, 24, or 32 bytes): ")
    text = input("Enter the text: ")

    if choice == 1:
        encrypted_text = encrypt(text, key)
        print("Encrypted Text:", encrypted_text)
    elif choice == 2:
        decrypted_text = decrypt(text, key)
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid choice. Please select 1 for encryption or 2 for decryption.")

def encrypt(plaintext, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, IV=key.encode('utf-8'))
    padded_text = pad(plaintext)
    encrypted_bytes = cipher.encrypt(padded_text.encode('utf-8'))
    return base64.b64encode(cipher.iv + encrypted_bytes).decode('utf-8') 
def decrypt(ciphertext, key):
    ciphertext_bytes = base64.b64decode(ciphertext.encode('utf-8'))
    iv = ciphertext_bytes[:16]  # Extract the IV
    ciphertext_bytes = ciphertext_bytes[16:]  # Remove the IV
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    decrypted_bytes = cipher.decrypt(ciphertext_bytes)
    decrypted_text = unpad(decrypted_bytes.decode('utf-8'))
    return decrypted_text

def pad(text):
    pad_length = 16 - len(text) % 16
    return text + pad_length * chr(pad_length)

def unpad(text):
    pad_length = ord(text[-1])
    return text[:-pad_length]

if __name__ == "__main__":
    main()

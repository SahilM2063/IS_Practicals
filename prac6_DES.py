from Crypto.Cipher import DES
import base64

def main():
    print("Choose an option:")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = int(input())
    key = input("Enter the key (8 characters): ")
    text = input("Enter the text: ")

    if len(key) != 8:
        print("Key must be 8 characters long.")
        return

    if choice == 1:
        encrypted_text = encrypt(text, key)
        print("Encrypted Text:", encrypted_text)
    elif choice == 2:
        decrypted_text = decrypt(text, key)
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid choice. Please select 1 for encryption or 2 for decryption.")
def encrypt(plaintext, key):
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    padded_text = pad(plaintext)
    encrypted_bytes = cipher.encrypt(padded_text.encode('utf-8'))
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def decrypt(ciphertext, key):
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    decrypted_bytes = cipher.decrypt(base64.b64decode(ciphertext.encode('utf-8')))
    decrypted_text = unpad(decrypted_bytes.decode('utf-8'))
    return decrypted_text

def pad(text):
    pad_length = 8 - len(text) % 8
    return text + pad_length * chr(pad_length)

def unpad(text):
    pad_length = ord(text[-1])
    return text[:-pad_length]

if __name__ == "__main__":
    main()

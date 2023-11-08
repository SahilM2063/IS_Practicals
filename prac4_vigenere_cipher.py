def encrypt_vigenere(plain_text, key):
    encrypted_text = []
    key_length = len(key)

    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            key_char = key[i % key_length]

            if char.isupper():
                offset = ord('A')
            elif char.islower():
                offset = ord('a')

            encrypted_char = chr((ord(char) + ord(key_char) - 2 * offset) % 26 + offset)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)

def decrypt_vigenere(encrypted_text, key):
    decrypted_text = []
    key_length = len(key)

    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            if char.isupper():
                offset = ord('A')
            elif char.islower():
                offset = ord('a')
            decrypted_char = chr((ord(char) - ord(key_char) + 26) % 26 + offset)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)

if __name__ == "__main__":
    choice = input("Choose an option (1 for encryption, 2 for decryption): ")

    if choice == '1':
        plain_text = input("Enter the text to encrypt: ")
        key = input("Enter the encryption key: ")
        encrypted_text = encrypt_vigenere(plain_text, key)
        print("Encrypted text:", encrypted_text)
    elif choice == '2':
        encrypted_text = input("Enter the text to decrypt: ")
        key = input("Enter the decryption key: ")
        decrypted_text = decrypt_vigenere(encrypted_text, key)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice. Please choose 1 for encryption or 2 for decryption.")

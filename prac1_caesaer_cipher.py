def caesar_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)

plain_text = input("Enter the plain text: ")
key = int(input("Enter the key (positive or negative integer): "))

encrypted_text = caesar_encrypt(plain_text, key)
print(f"Encrypted text: {encrypted_text}")

decrypted_text = caesar_decrypt(encrypted_text, key)
print(f"Decrypted text: {decrypted_text}")

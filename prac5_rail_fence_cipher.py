def encrypt_rail_fence(plain_text, rails):
    fence = [[' ' for _ in range(len(plain_text))] for _ in range(rails)]
    direction = -1  # Direction for moving up or down
    row = 0

    for char in plain_text:
        fence[row][row] = char
        if row == 0 or row == rails - 1:
            direction = -direction
        row += direction

    encrypted_text = ''.join(''.join(row) for row in fence)
    return encrypted_text

def decrypt_rail_fence(encrypted_text, rails):
    fence = [[' ' for _ in range(len(encrypted_text))] for _ in range(rails)]
    direction = -1
    row = 0

    for i in range(len(encrypted_text)):
        fence[row][i] = 'X'
        if row == 0 or row == rails - 1:
            direction = -direction
        row += direction

    index = 0
    for i in range(rails):
        for j in range(len(encrypted_text)):
            if fence[i][j] == 'X' and index < len(encrypted_text):
                fence[i][j] = encrypted_text[index]
                index += 1
        direction = -1
        row = 0

    decrypted_text = ''
    for i in range(len(encrypted_text)):
        decrypted_text += fence[row][i]
        if row == 0 or row == rails - 1:
            direction = -direction
        row += direction

    return decrypted_text

if __name__ == "__main__":
    choice = input("Choose an option (1 for encryption, 2 for decryption): ")

    if choice == '1':
        plain_text = input("Enter the text to encrypt: ")
        rails = int(input("Enter the number of rails: "))
        encrypted_text = encrypt_rail_fence(plain_text, rails)
        print("Encrypted text:", encrypted_text)
    elif choice == '2':
        encrypted_text = input("Enter the text to decrypt: ")
        rails = int(input("Enter the number of rails: "))
        decrypted_text = decrypt_rail_fence(encrypted_text, rails)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice. Please choose 1 for encryption or 2 for decryption.")

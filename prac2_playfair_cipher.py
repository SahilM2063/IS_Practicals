import string

def clean_text(text):
    text = text.replace(" ", "").upper()
    text = text.replace("J", "I")
    text = text.replace(" ", "")
    return text

def build_playfair_matrix(key):
    key = clean_text(key)
    alphabet = string.ascii_uppercase.replace("J", "")
    matrix = []
    for letter in key:
        if letter not in matrix and letter in alphabet:
            matrix.append(letter)
    for letter in alphabet:
        if letter not in matrix:
            matrix.append(letter)
    matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return matrix

def find_letter_position(matrix, letter):
    for row in range(5):
        if letter in matrix[row]:
            return row, matrix[row].index(letter)
    return -1, -1

def playfair_encrypt(text, matrix):
    text = clean_text(text)

    if len(text) % 2 != 0:
        text += 'X'  # Pad with 'X' if the text length is odd 
    encrypted_text = ""
    for i in range(0, len(text), 2):
        letter1, letter2 = text[i], text[i + 1]
        row1, col1 = find_letter_position(matrix, letter1)
        row2, col2 = find_letter_position(matrix, letter2)

        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]

    return encrypted_text

def playfair_decrypt(text, matrix):
    text = clean_text(text)
    decrypted_text = ""
    
    for i in range(0, len(text), 2):
        letter1, letter2 = text[i], text[i + 1]
        row1, col1 = find_letter_position(matrix, letter1)
        row2, col2 = find_letter_position(matrix, letter2)
        
        if row1 == row2:
            decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]

    return decrypted_text 
# Get the Playfair cipher key from the user
key = input("Enter the Playfair cipher key (no spaces, only uppercase letters): ")

# Build the Playfair matrix
matrix = build_playfair_matrix(key)

# Display the Playfair key matrix
print("Playfair Cipher Key Matrix:")
for row in matrix:
    print(" ".join(row))

# Get the plain text from the user
plain_text = input("Enter the plain text: ")

# Encrypt the text
encrypted_text = playfair_encrypt(plain_text, matrix)
print(f"Encrypted text: {encrypted_text}")

# Decrypt the text
decrypted_text = playfair_decrypt(encrypted_text, matrix)
print(f"Decrypted text: {decrypted_text}")

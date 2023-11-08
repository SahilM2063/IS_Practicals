def main():
    plain_text = input("Enter the plain text: ").upper().replace(" ", "")
    while len(plain_text) % 3 != 0:
        plain_text += 'X'
    
    key = [[0] * 3 for _ in range(3)]
    print("Enter the 3x3 key matrix:")
    for i in range(3):
        for j in range(3):
            key[i][j] = int(input(f"Enter key element at position ({i + 1}, {j + 1}):"))
    
    cipher_text = hill_cipher(plain_text, key)
    print("Cipher Text:", cipher_text)

def hill_cipher(plain_text, key):
    cipher_text = ""
    for i in range(0, len(plain_text), 3):
        group = plain_text[i:i + 3]
        group_vector = [ord(char) - ord('A') for char in group]
        result_vector = [0, 0, 0]
        
        for j in range(3):
            for k in range(3):
                result_vector[j] += key[j][k] * group_vector[k]
            result_vector[j] %= 26
        
        for j in range(3):
            cipher_text += chr(result_vector[j] + ord('A'))
    
    return cipher_text
    
if _name_ == "_main_":
    main()
        


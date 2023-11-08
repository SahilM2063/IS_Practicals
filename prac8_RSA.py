import random

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to find the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find the modular multiplicative inverse
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None 
# Function to generate RSA keys
def generate_rsa_keys():
    while True:
        p = random.randint(100, 200)
        if is_prime(p):
            break
    while True:
        q = random.randint(200, 300)
        if is_prime(q):
            break

    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break

    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

# Function to encrypt a message
def encrypt(message, public_key):
    e, n = public_key
    encrypted = [pow(ord(char), e, n) for char in message]
    return encrypted
 # Function to decrypt a message
def decrypt(encrypted, private_key):
    d, n = private_key
    decrypted = [chr(pow(char, d, n)) for char in encrypted]
    return ''.join(decrypted)

if __name__ == "__main__":
    # Generate RSA keys
    public_key, private_key = generate_rsa_keys()

    # Input message
    message = input("Enter a message to encrypt: ")

    # Encrypt the message
    encrypted_message = encrypt(message, public_key)
    print("Encrypted message:", encrypted_message)

    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, private_key)
    print("Decrypted message:", decrypted_message)

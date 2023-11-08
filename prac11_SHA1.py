import hashlib

# Prompt the user for input
input_string = input("Enter a string to generate a SHA-1 hash: ")

# Create a SHA-1 hash object
sha1_hash = hashlib.sha1()

# Update the hash object with the input string
sha1_hash.update(input_string.encode())

# Get the hexadecimal representation of the hash
hash_hex = sha1_hash.hexdigest()

print("SHA-1 hash:", hash_hex)

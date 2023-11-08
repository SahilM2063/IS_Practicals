import hashlib

# Prompt the user for input
input_string = input("Enter a string to generate an MD5 hash: ")

# Create an MD5 hash object
md5_hash = hashlib.md5()

# Update the hash object with the input string
md5_hash.update(input_string.encode())

# Get the hexadecimal representation of the hash
hash_hex = md5_hash.hexdigest()

print("MD5 hash:", hash_hex)

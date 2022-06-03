# import the library module
import hashlib
import clipboard
# pip install clipboard

# initialize a string
clave = input("Private Key:")
str = "publicKey" + privateKey
# Change "publicKey" to a default key, Ejp: old password
# Insert Private Key, Ejp: You are registering in Facebook the key could be "Facebook"

# encode the string
encoded_str = str.encode()
 
# create sha-2 hash objects initialized with the encoded string
hash_obj_sha256 = hashlib.sha256(encoded_str).hexdigest()   # SHA256
hash_obj_sha512 = hashlib.sha512(encoded_str).hexdigest()   # SHA512

# Capitalize some words
hash_obj_sha256 = hash_obj_sha256.encode("utf-8").replace(b"a", b"A").decode('utf-8')
hash_obj_sha512 = hash_obj_sha512.encode("utf-8").replace(b"a", b"A").decode('utf-8')

# The symbols "@$" could be changed to others
print("\nSHA256 Hash: ", hash_obj_sha256 + "@$")
print("\nSHA512 Hash: ", hash_obj_sha512 + "@$")

# Copy to clipboard the hash with algorithm sha512
clipboard.copy(hash_obj_sha512+ "@$")

# Append Private key to a file to remember keys, opcionally
f = open ('clave.txt','a')
f.write('\n' + clave)
f.close()

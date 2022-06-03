# import the library module
import hashlib
import clipboard
# pip install clipboard

# initialize a string
clave = input("Private Key:")
str = "publicKey" + privateKey
# publicKey = Key that will be saved on your computer, you could use an old password, don't forget.
# privateKey = could be the name of the page you register to, it should be easy to remember.

# encode the string
encoded_str = str.encode()
 
# create sha-2 hash objects initialized with the encoded string
# Hashing algorithms can be changed: https://docs.python.org/3/library/hashlib.html
hash_obj_sha256 = hashlib.sha256(encoded_str).hexdigest()   # SHA256
hash_obj_sha512 = hashlib.sha512(encoded_str).hexdigest()   # SHA512

# Capital more or different letters
hash_obj_sha256 = hash_obj_sha256.encode("utf-8").replace(b"a", b"A").decode('utf-8')
hash_obj_sha512 = hash_obj_sha512.encode("utf-8").replace(b"a", b"A").decode('utf-8')

# You can change the symbols for more or different, and not only at the end of the password.
print("\nSHA256 Hash: ", hash_obj_sha256 + "@$")
print("\nSHA512 Hash: ", hash_obj_sha512 + "@$")

# Copy to clipboard the hash with algorithm sha512
clipboard.copy(hash_obj_sha512+ "@$")

# Remove keyword saving, if you seems it unsafe
# The private key would not be private
f = open ('clave.txt','a')
f.write('\n' + clave)
f.close()

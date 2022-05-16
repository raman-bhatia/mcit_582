def encrypt(key,plaintext):
    ciphertext=""
    for char in plaintext:
        ciphertext += chr((ord(char) + key - 65) % 26 + 65) 
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    for char in ciphertext:
        plaintext += chr((ord(char) - key - 65) % 26 + 65)
    return plaintext

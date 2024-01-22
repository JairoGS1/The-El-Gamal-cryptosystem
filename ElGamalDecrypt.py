import random

def decrypt(p, x, ciphertext):
    ga, cipher = ciphertext
    k = pow(ga, x)
    inv_k = pow(k, -1, p)
    decrypted_chars = []
    for char in cipher:
        decrypted_chars += [chr((char * inv_k) % p)] 
    decrypted_message = ''.join(decrypted_chars)
    return decrypted_message

p = int(input("Enter the value of p: "))
x = int(input("Enter the value of x (private key): "))

# Enter the encrypted message obtained from elgamal_encrypt
y = int(input("Enter the value of y (public key): "))
ciphertext_pairs = []

while True:
    try:
        c2 = int(input("Enter the value of c2 (0 to finish): "))
        if c2 == 0:
            break
        ciphertext_pairs.append(c2)
    except ValueError:
        print("Please enter integer values.")

ciphertext = (y, ciphertext_pairs)

decrypted_message = decrypt(p, x, ciphertext)
print(f"\nDecrypted Message: {decrypted_message}")

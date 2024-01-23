import random

def elgamal_encrypt(p, g, gx, text):
    text2int = text_to_integer(text)
    a = random.randint(1, p-1)
    ga = pow(g, a)
    k = pow(gx, a)
    result = []
    for char in text2int:
        result += [(k * char) % p]
    return ga, result

def text_to_integer(text):
    integers = []
    for char in text:
        integers += [ord(char)]
    return integers

p = int(input("Enter the value of p: "))
g = int(input("Enter the value of g: "))
gx = int(input("Enter the value of gx (public key): "))
plaintext = input("Enter the text to encrypt (UTF-8): ")

public_key, ciphertext = elgamal_encrypt(p, g, gx, plaintext)
print(f"\nPublic Key (gy): {public_key}")
print("Encrypted Message:")
for pair in ciphertext:
    print(f"({public_key}, {pair})")

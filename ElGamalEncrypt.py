import random

def elgamal_encrypt(p, g, gx, text):
    text2int = text_integer(text)
    print(text2int)
    a = random.randint(1, p-1)
    ga = pow(g, a)
    k = pow(gx, a)
    result = []
    for char in text2int:
        result += [(k * char) % p]
    return ga, result

def text_integer(text):
    integers = []
    for char in text:
        integers += [ord(char)]
    return integers

p = int(input("Entra el valor de p: "))
g = int(input("Entra el valor de g: "))
gx = int(input("Entra el valor de gx (clau pública): "))
plaintext = input("Introdueix el text a encriptar (UTF-8): ")

public_key, ciphertext = elgamal_encrypt(p, g, gx, plaintext)
print(f"\nClau pública (gy): {public_key}")
print("Missatge encriptat:")
for pair in ciphertext:
    print(f"({public_key}, {pair})")

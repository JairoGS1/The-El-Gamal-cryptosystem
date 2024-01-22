import random

def elgamal_encrypt(p, g, gx, text):
    text2int = text_integer(text)
    a = 3
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

def Decrypt(p, x, ciphertext):
    ga, cipher = ciphertext
    #print(ga)
    k = pow(ga, x)
    inv_k = pow(k, -1, p)
    result = []
    for char in cipher:
        result += [(char * inv_k) % p] 
    return result

p = int(input("Entra el valor de p: "))
g = int(input("Entra el valor de g: "))
gx = int(input("Entra el valor de gx (clau pública): "))
x = int(input("Entra el valor de x (clau privada): "))
plaintext = input("Introdueix el text a encriptar (UTF-8): ")

public_key, ciphertext = elgamal_encrypt(p, g, gx, plaintext)
print(f"\nClau pública (y): {public_key}")
print("Missatge encriptat:")
for pair in ciphertext:
    print(f"({public_key}, {pair})")

print(Decrypt(p, x, ciphertext))

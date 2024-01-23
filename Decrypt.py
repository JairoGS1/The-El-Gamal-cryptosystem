import random

def Decrypt(p, x, ciphertext):
    ga, cipher = ciphertext
    k = pow(ga, x)
    inv_k = pow(k, -1, p)
    decripted_char = []
    print(cipher)
    for char in cipher:
        decripted_char += [chr((char * inv_k) % p)] 
    decrypted_message = ''.join(decripted_char)
    return decrypted_message

p = int(input("Entra el valor de p: "))
x = int(input("Entra el valor de x (clau privada): "))

# Introdueix el missatge encriptat amb elgamal_encrypt
y = int(input("Entra el valor de y (clau pública): "))
ciphertext_pairs = []

while True:
    try:
        c2 = int(input("Entra el valor de c2 (0 per acabar): "))
        if c2 == 0:
            break
        ciphertext_pairs.append((c2))
    except ValueError:
        print("Si us plau, introdueix nombres enters.")

ciphertext = (y, ciphertext_pairs)

decrypted_message = Decrypt(p, x, ciphertext)
print(f"\nMissatge desencriptat: {decrypted_message}")

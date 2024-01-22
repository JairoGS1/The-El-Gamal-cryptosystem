import random
import math

def is_coprime(a, b):
    return math.gcd(a, b) == 1

def is_primitive_root(g, p):
    Euler = p - 1
    if not is_coprime(g, p):
        return False
    order = order_g(g, p)
    return order == Euler

def order_g(g, p):
    current_g = g
    for order in range(p - 1):
        if current_g % p == 1:
            return order + 1
        else:
            current_g = (current_g * g) % p
    return p - 1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def input_prime(prompt):
    while True:
        try:
            value = int(input(prompt))
            if is_prime(value):
                return value
            else:
                raise ValueError(f"{value} is not a prime number.")
        except ValueError as e:
            print(f"Error: {e} Please enter a prime number.")

def input_primitive_root(prompt, p):
    while True:
        try:
            value = int(input(prompt))
            if is_primitive_root(value, p):
                return value
            else:
                raise ValueError(f"{value} is not a primitive root modulo {p}.")
        except ValueError as e:
            print(f"Error: {e} Please enter a primitive root mod {p}.")

def input_in_range(prompt, p):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value < p:
                return value
            else:
                raise ValueError(f"{value} is not in the range [1, {p-1}].")
        except ValueError as e:
            print(f"Error: {e} Please enter a value in the range [1, {p-1}].")

def generate_private_key(p):
    return random.randint(1, p-1)

def calculate_public_key(g, x, p):
    return pow(g, x, p)

def elgamal_encrypt(p, g, x, plaintext):
    a = generate_private_key(p)
    ga = calculate_public_key(g, a, p)
    k = pow(pow(g,x,p), a, p)
    c = (plaintext * k) % p
    return ga, c

def elgamal_decrypt(p, x, ga, c):
    k = pow(ga, x, p)
    k_inverse = pow(k, -1, p)
    decrypted_message = (c * k_inverse) % p
    return decrypted_message

# Inputs
p = input_prime("Enter the value of p (prime): ")
g = input_primitive_root("Enter the value of g (primitive root mod p): ", p)
b =input_in_range("Enter a number between 1 and p-1: ", p)
text = input("Enter the plaintext message (integer): ")

utf8_encoded = text.encode('utf-8')
plaintext=[int(byte) for byte in utf8_encoded]

# Encryption
ga, c = elgamal_encrypt(p, g, b, plaintext)

# Decryption
decrypted_message = elgamal_decrypt(p, b, ga, c)

# Output
print(f"Encrypted message: (ga={ga}, c={c})")
print(f"Decrypted message: {decrypted_message}")

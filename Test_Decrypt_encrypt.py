import random
import math
from Primitive_root import is_prime, is_coprime, is_primitive_root, order_g, input_prime
from FME_Algorithm import fast_modular_exponentiation_update

# Function to check if a value can be converted to an integer
def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# Function to check if a string contains only ASCII characters
def is_ascii(text):
    return all(32 <= ord(char) <= 126 for char in text)

# Function to input a primitive root with error handling
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

# Function to input an integer within a specified range
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

# Function to input an integer with error handling
def input_integer(prompt):
    while True:
        try:
            value = input(prompt)
            if is_integer(value):
                return int(value)
            else:
                raise ValueError("Please enter a valid integer.")
        except ValueError as e:
            print(f"Error: {e}")

# Function to input a string containing only ASCII characters
def input_ascii_string(prompt):
    while True:
        try:
            text = input(prompt)
            if is_ascii(text):
                return text
            else:
                raise ValueError("Please enter a string containing only ASCII characters.")
        except ValueError as e:
            print(f"Error: {e}")

# Function to group a list of integers into a list of integers with a specified length
def group_list(lst, n):
    grouped_list = []
    while len(lst) % n != 0:
        lst.append(0)
    for i in range(0, len(lst), n): 
        group = lst[i:i+n]
        grouped_list.append(int(''.join(map(str, group))))
    return grouped_list

# Function to generate a private key in the range [1, p-1]
def generate_private_key(p):
    return random.randint(1, p-1)

# Function to calculate the public key using modular exponentiation
def calculate_public_key(g, x, p):
    return fast_modular_exponentiation_update(g, x, p)

# Function to perform ElGamal encryption
def elgamal_encrypt(p, g, x, a, text):
    k = fast_modular_exponentiation_update(fast_modular_exponentiation_update(g,x,p), a, p)
    c = (text * k) % p
    ga = calculate_public_key(g, a, p)
    return ga, c

# Function to perform ElGamal decryption
def elgamal_decrypt(p, x, ga, c):
    k = fast_modular_exponentiation_update(ga, x, p)
    k_inverse = pow(k, -1, p)
    decrypted_message = (c * k_inverse) % p
    return decrypted_message

# Function to encrypt a list of integers using ElGamal encryption
def encrypt_list(p, g, x, a, int_list):
    encrypted_values = []
    for val in int_list:
        ga, c = elgamal_encrypt(p, g, x, a, val)
        encrypted_values.append(c)
    return encrypted_values

# Function to separate characters from a decrypted message
def separate_characters(decrypt_mess):
    char_list = []
    int_list = []
    for i in decrypt_mess:
        int_list.append(i)
        integer = int("".join(map(str,int_list)))
        if int(integer > 30):
            char_list.append(integer)
            int_list = []
    return char_list

# Function to decrypt a list of encrypted values using ElGamal decryption
def decrypt_list(p, x, ga, encrypted_values, n):
    decrypted_values = []
    for c in encrypted_values:
        decrypted_message = elgamal_decrypt(p, x, ga, c)
        decrypted_digits = [int(d) for d in str(decrypted_message).zfill(n)]
        decrypted_characters = separate_characters(decrypted_digits)
        decrypted_values.extend(decrypted_characters)
        result = ''.join(map(chr, decrypted_values))
    return result

if __name__=='__main__':
    # Inputs
    p = input_prime("Enter the value of p (prime): ")
    g = input_primitive_root("Enter the value of g (primitive root mod p): ", p)
    b = input_in_range("Enter a number between 1 and p-1 (secret key b): ", p)
    text = input_ascii_string("Enter the plaintext message (ascii): ")

    utf8_encoded = text.encode('utf-8')
    plaintext = [int(byte) for byte in utf8_encoded]

    # Generate public and private keys
    a = random.randint(1, p-2)
    ga = calculate_public_key(g, a, p)

    # Obtain the split string
    n = input_integer("Enter the value of n where n is the string length: ")
    text_list = group_list(plaintext, n)
    
    # Encryption
    encrypted_values = encrypt_list(p, g, b, a, text_list)

    # Decryption
    decrypted_message = decrypt_list(p, b, ga, encrypted_values, n)

    # Output
    print(f"Encrypted message: (ga={ga}, c={encrypted_values})")
    print(f"Decrypted message: {decrypted_message}")

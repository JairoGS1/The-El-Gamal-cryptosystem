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

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_ascii(text):
    return all(32 <= ord(char) <= 126 for char in text)

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

def group_list(lst, n):
    grouped_list = []
    while len(lst) % n != 0:
        lst.append(0)
    for i in range(0, len(lst), n): 
        group = lst[i:i+n]
        grouped_list.append(int(''.join(map(str, group))))
    return grouped_list

def generate_private_key(p):
    return random.randint(1, p-1)

def calculate_public_key(g, x, p):
    return pow(g, x, p)

def elgamal_encrypt(p, g, x, a, text):
    k = pow(pow(g,x,p), a, p)
    c = (text * k) % p
    return ga, c

def elgamal_decrypt(p, x, ga, c):
    k = pow(ga, x, p)
    k_inverse = pow(k, -1, p)
    decrypted_message = (c * k_inverse) % p
    return decrypted_message

def encrypt_list(p, g, x, a, int_list):
    encrypted_values = []
    for val in int_list:
        ga, c = elgamal_encrypt(p, g, x, a, val)
        encrypted_values.append(c)
    return encrypted_values

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
    b =input_in_range("Enter a number between 1 and p-1 (secret key b): ", p)
    text = input_ascii_string("Enter the plaintext message (ascii): ")

    utf8_encoded = text.encode('utf-8')
    plaintext=[int(byte) for byte in utf8_encoded]

    #Generate public and privte key
    a = random.randint(1, p-2)
    ga = calculate_public_key(g, a, p)

    #Obtain the split string
    n = input_integer("Enter the value of n where n is the string length: ")
    text_list=group_list(plaintext,n)
    print("texto junto: ", text_list)
    
    # Encryption
    encrypted_values=encrypt_list(p,g,b,a,text_list)

    # Decryption
    print("valores encriptados: ",encrypted_values)
    decrypted_message = decrypt_list(p, b, ga, encrypted_values, n)

    # Output
    print(f"Encrypted message: (ga={ga}, c={encrypted_values})")
    print(f"Decrypted message: {decrypted_message}")

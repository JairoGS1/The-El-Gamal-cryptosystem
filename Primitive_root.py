import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_coprime(a, b):
    return math.gcd(a, b) == 1

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

def input_coprime(prompt, p):
    while True:
        try:
            value = int(input(prompt))
            if is_coprime(value, p):
                return value
            else:
                raise ValueError(f"{value} is not coprime with {p}.")
        except ValueError as e:
            print(f"Error: {e} Please enter a coprime number.")

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

p = input_prime("Enter a prime number for p: ")
g = input_coprime(f"Enter the value of g (coprime with {p}): ", p)

if is_primitive_root(g, p):
    print(f"{g} is a primitive root modulo {p}.")
else:
    print(f"{g} is not a primitive root modulo {p}. Please try again.")

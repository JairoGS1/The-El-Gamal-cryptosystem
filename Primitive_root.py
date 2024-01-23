import math

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if two numbers are coprime
def is_coprime(a, b):
    return math.gcd(a, b) == 1

# Function to input a prime number with error handling
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

# Function to input a coprime number with error handling
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

# Function to check if a number is a primitive root modulo p
def is_primitive_root(g, p):
    Euler = p - 1
    # Check if g is coprime with p
    if not is_coprime(g, p):
        return False
    # Calculate the order of g modulo p and check if it equals Euler's totient function value
    order = order_g(g, p)
    return order == Euler

# Function to calculate the order of g modulo p
def order_g(g, p):
    current_g = g
    for order in range(p - 1):
        # Check if the current power of g is congruent to 1 modulo p
        if current_g % p == 1:
            return order + 1
        else:
            current_g = (current_g * g) % p
    # If no order is found, return p - 1 (Euler's totient function value)
    return p - 1

if __name__=='__main__':
    p = input_prime("Enter a prime number for p: ")
    g = input_coprime(f"Enter the value of g (coprime with {p}): ", p)
    
    # Check if g is a primitive root modulo p
    if is_primitive_root(g, p):
        print(f"{g} is a primitive root modulo {p}.")
    else:
        print(f"{g} is not a primitive root modulo {p}. Please try again.")


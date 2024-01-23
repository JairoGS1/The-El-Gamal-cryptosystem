import time
import math

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is in Z/pZ
def is_in_zpz(g, p):
    return 0 < g < p

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

# Function to input a value in Z/pZ with error handling
def input_in_zpz(prompt, p):
    while True:
        try:
            value = int(input(prompt))
            if is_in_zpz(value, p):
                return value
            else:
                raise ValueError(f"{value} is not in Z/{p}Z.")
        except ValueError as e:
            print(f"Error: {e} Please enter a value in Z/{p}Z.")

# Bad solution for modular exponentiation (O(e) time complexity)
def fast_modular_exponentiation(g, e, p):
  result = g
  for exp in range(e-1):
    result = (result*g) % p
  return result

# Efficient solution for modular exponentiation using binary exponentiation (O(log(e) time complexity)
def fast_modular_exponentiation_update(g, e, p):
    result = 1
    # Convert the exponent to binary
    binary_e = bin(e)[2:]
    # Iterate over the bits of the exponent (from right to left)
    for bit in binary_e[::-1]:
        if bit == '1':
            result = (result * g) % p
        g = (g * g) % p
    return result

if __name__=='__main__':
    p = input_prime("Enter the value of p (prime): ")
    g = input_in_zpz("Enter the value of g (in Z/pZ): ", p)
    e = input_prime("Enter the value of e (prime): ")
    
    # Measure the execution time of the inefficient modular exponentiation
    inici_temps2 = time.time()
    resultat2 = fast_modular_exponentiation_update(g, e, p)
    fi_temps2 = time.time()
    temps_total2 = fi_temps2 - inici_temps2
    print(f"The result2 {g}^{e} (mod {p}) is: {resultat2}")
    print(f"Execution time2: {temps_total2} seconds")
    
    # Measure the execution time of the efficient modular exponentiation
    inici_temps = time.time()
    resultat = fast_modular_exponentiation(g, e, p)
    fi_temps = time.time()
    temps_total = fi_temps - inici_temps
    print(f"The result {g}^{e} (mod {p}) is: {resultat}")
    print(f"Execution time: {temps_total} seconds")


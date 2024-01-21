def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
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

def extended_euclidean(p, q):
    if q == 0:
        return p, 1, 0
    else:
        gcd, alpha, beta = extended_euclidean(q, p % q)
        new_alpha = beta
        new_beta = alpha - (p // q) * beta
        return gcd, new_alpha, new_beta

# Take user input for p and q, ensuring they are prime
p = input_prime("Enter a prime number for p: ")
q = input_prime("Enter a prime number for q: ")

gcd, alpha, beta = extended_euclidean(p, q)

print(f"The GCD of {p} and {q} is: {gcd}")
print(f"Alpha ({p}) + Beta ({q}) = GCD: {alpha}*{p} + {beta}*{q} = {gcd}")


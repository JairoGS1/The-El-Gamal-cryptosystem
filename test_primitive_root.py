from Primitive_root import is_prime, is_coprime, is_primitive_root

# Test is_prime
print("Testing is_prime:")
print(f"Is 17 prime? {is_prime(17)}")  # True
print(f"Is 25 prime? {is_prime(25)}")  # False
print(f"Is 2 prime? {is_prime(2)}")    # True
print()

# Test is_coprime
print("Testing is_coprime:")
print(f"Are 3 and 10 coprime? {is_coprime(3, 10)}")  # True
print(f"Are 4 and 9 coprime? {is_coprime(4, 9)}")    # True
print(f"Are 7 and 14 coprime? {is_coprime(7, 14)}")  # False
print()

# Test is_primitive_root
print("Testing is_primitive_root:")
p_value = 17
g_value = 3
print(f"Is {g_value} a primitive root modulo {p_value}? {is_primitive_root(g_value, p_value)}")  # True
g_value = 4
print(f"Is {g_value} a primitive root modulo {p_value}? {is_primitive_root(g_value, p_value)}")  # False

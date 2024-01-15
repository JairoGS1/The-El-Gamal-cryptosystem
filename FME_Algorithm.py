import time
#Bad solution O(e)
def fast_modular_exponentiation(g, e, p):
  retult = g
  for exp in range(e-1):
    result = (result*g) % p
  return result

# Time complexity: O(log(e))
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

p = int(input("Enter the value of p: "))
g = int(input("Enter the value of g: "))
e = int(input("Enter the value of e: "))

inici_temps2 = time.time()
resultat2 = fast_modular_exponentiation_update(g, e, p)
fi_temps2 = time.time()
temps_total2 = fi_temps2 - inici_temps2
print(f"The result2 {g}^{e} (mod {p}) is: {resultat2}")
print(f"Execution time2: {temps_total2} seconds")

inici_temps = time.time()
resultat = fast_modular_exponentiation(g, e, p)
fi_temps = time.time()
temps_total = fi_temps - inici_temps
print(f"The result {g}^{e} (mod {p}) is: {resultat}")
print(f"Execution time: {temps_total} seconds")

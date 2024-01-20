def is_primitive_root(g, p):
  Euler = p-1
  if math.gcd(g, p) != 1:
    return False
  order = order_g(g, p)
  if order == Euler:
    return True
  else:
    return False

def order_g(g, p):
  current_g = g
  for order in range(p-1):
    if current_g % p == 1:
      return (order+1)
    else:
      current_g = (current_g * g) % p
  return p-1

p = int(input("Entra el valor de p (primer): "))
g = int(input(f"Entra el valor de g (coprim amb {p}): "))

if is_primitive_root(g, p):
    print(f"{g} és una arrel primitiva mòdul {p}.")
else:
    print(f"{g} no és una arrel primitiva mòdul {p}.")

def is_primitive_root(p, g):
  Euler = p-1
  if math.gcd(g, p) != 1:
    return False
  order = order(p, g)
  if order == Euler:
    return True
  else:
    return False

def order(p, g):
  current_g = g
  for order in range(p-1):
    if current_g % p == 1:
      return order
    else:
      current_g = (current_g * g) % p
  return p-1

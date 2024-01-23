from FME_Algorithm import is_prime, is_in_zpz, fast_modular_exponentiation, fast_modular_exponentiation_update

def test_is_prime():
    # Test cases for the is_prime function
    assert is_prime(2) == True
    assert is_prime(17) == True
    assert is_prime(97) == True
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(16) == False

def test_is_in_zpz():
    # Test cases for the is_in_zpz function
    assert is_in_zpz(3, 7) == True
    assert is_in_zpz(1, 7) == True
    assert is_in_zpz(7, 7) == False
    assert is_in_zpz(8, 7) == False

def test_fast_modular_exponentiation():
    # Test cases for the fast_modular_exponentiation function
    assert fast_modular_exponentiation(2, 3, 5) == 3
    assert fast_modular_exponentiation(3, 3, 5) == 2

def test_fast_modular_exponentiation_update():
    # Test cases for the fast_modular_exponentiation_update function
    assert fast_modular_exponentiation_update(2, 3, 5) == 3
    assert fast_modular_exponentiation_update(3, 3, 5) == 2


# Execute the tests
test_is_prime()
test_is_in_zpz()
test_fast_modular_exponentiation()
test_fast_modular_exponentiation_update()
print("All tests passed!")


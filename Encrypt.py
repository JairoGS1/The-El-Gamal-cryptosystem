import random

def elgamal_encrypt(p, g, gx, text):
    # Convert the input text to a list of integers using ASCII values
    text2int = text_to_integer(text)
    
    # Generate a random number 'a' in the range [1, p-1]
    a = random.randint(1, p-1)
    
    # Calculate 'ga' (public key) and 'k' (shared secret key)
    ga = pow(g, a, p)
    k = pow(gx, a, p)
    
    result = []
    # Encrypt each integer in the input text using the shared secret key 'k'
    for char in text2int:
        result += [(k * char) % p]
    
    # Return the public key 'ga' and the list of encrypted pairs
    return ga, result

def text_to_integer(text):
    # Convert each character in the input text to its ASCII value
    integers = [ord(char) for char in text]
    return integers

if __name__=='__main__':
    # Get input for prime number 'p', generator 'g', and public key 'gx'
    p = int(input("Enter the value of p: "))
    g = int(input("Enter the value of g: "))
    gx = int(input("Enter the value of gx (public key): "))
    plaintext = input("Enter the text to encrypt (UTF-8): ")
    
    # Call the elgamal_encrypt function to get the public key and encrypted pairs
    public_key, ciphertext = elgamal_encrypt(p, g, gx, plaintext)
    
    # Print the public key and the list of encrypted pairs
    print(f"\nPublic Key (gy): {public_key}")
    print("Encrypted Message:")
    for pair in ciphertext:
        print(f"({public_key}, {pair})")

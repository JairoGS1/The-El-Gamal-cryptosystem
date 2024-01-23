import random

def Decrypt(p, x, ciphertext):
    # Unpack the ciphertext into 'ga' (public key) and 'cipher' (list of encrypted characters)
    ga, cipher = ciphertext
    # Calculate the shared secret key 'k' using the public key 'ga' and private key 'x'
    k = pow(ga, x, p)
    # Calculate the modular inverse of 'k' (inv_k)
    inv_k = pow(k, -1, p)
    decrypted_char = []
    
    # Iterate through each character in the encrypted message
    for char in cipher:
        # Decrypt each character using the modular inverse 'inv_k' and modulo 'p'
        decrypted_char += [chr((char * inv_k) % p)] 
    
    # Join the decrypted characters to form the decrypted message
    decrypted_message = ''.join(decrypted_char)
    return decrypted_message

if __name__=='__main__':
    # Get input for prime number 'p' and private key 'x'
    p = int(input("Enter the value of p: "))
    x = int(input("Enter the value of x (private key): "))
    
    # Get input for public key 'y' and the list of encrypted characters 'ciphertext_pairs'
    y = int(input("Enter the value of y (public key): "))
    ciphertext_pairs = []
    
    # Input loop to collect the encrypted characters until 0 is entered
    while True:
        try:
            c2 = int(input("Enter the value of c2 (enter 0 to finish): "))
            if c2 == 0:
                break
            ciphertext_pairs.append(c2)
        except ValueError:
            print("Please enter integer values.")
    
    # Create a tuple containing the public key 'y' and the list of encrypted characters 'ciphertext_pairs'
    ciphertext = (y, ciphertext_pairs)
    
    # Call the Decrypt function to get the decrypted message
    decrypted_message = Decrypt(p, x, ciphertext)
    print(f"\nDecrypted Message: {decrypted_message}")

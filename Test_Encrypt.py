from Encrypt_Decrypt import *

def true_proof():
    p = 82589933
    g = 2
    b = 20
    text = "Bon dia a tots"
    utf8_encoded = text.encode('utf-8')
    plaintext=[int(byte) for byte in utf8_encoded]
    n = 3
    a = random.randint(1, p-2)
    ga = calculate_public_key(g, a, p)
    text_list=group_list(plaintext,n)
    encrypted_values=encrypt_list(p,g,b,a,text_list)
    decrypted_message = decrypt_list(p, b, ga, encrypted_values, n)
    print("Plane text without encryption: ", text)
    print(f"Encrypted message 1: (ga={ga}, c={encrypted_values})")
    print(f"Decrypted message 1: {decrypted_message}")

def false_proof():
    p = 11 #bad prime. Low value
    g = 2
    b = 20
    text = "Bon dia a tots"
    utf8_encoded = text.encode('utf-8')
    plaintext=[int(byte) for byte in utf8_encoded]
    n = 3
    a = random.randint(1, p-2)
    ga = calculate_public_key(g, a, p)
    text_list=group_list(plaintext,n)
    encrypted_values=encrypt_list(p,g,b,a,text_list)
    decrypted_message = decrypt_list(p, b, ga, encrypted_values, n)
    print("Plane text without encryption: ", text)
    print(f"Encrypted message 2: (ga={ga}, c={encrypted_values})")
    print(f"Bad decrypted message 2: {decrypted_message}") #Bad decrypt values


if __name__=='__main__':
    true_proof()
    print("---------------------------------------")
    false_proof()

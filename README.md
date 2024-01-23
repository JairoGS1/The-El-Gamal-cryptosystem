# ElGamal Cryptosystem

## Compilation and Execution Guide

### Download and install python
Go to the official Python website at https://www.python.org/downloads/ and download the latest version of Python 3.

## Execution of Python Codes
To execute Python codes from the command line:
  1. Open the Command Line:
     - On Windows, open "Command Prompt" or "PowerShell".
     - On Unix systems (Linux, macOS), open the "Terminal". 
  2.  Navigate to the Code Directory:
      - Use the cd command to change to the directory where the code is located.
  4.  Run the code:
      - Use the python3 command followed by the name of the Python file.
        
            python3 file_name.py

  6. Specific Instructions for Each Code
     - Fast Modular Exponentiation
       - Run the **_FME_Algorithm.py_** file.
       - Input the values of p and g when prompted.
     - Primitive Root
       - Run the **_Primitive.py_** file.
       - Input the values of p (prime number) and g (supposed primitive root) when prompted.
     - ElGamal Encrypting Module
       - Run the **_Encrypt.py_** file.
       - Input the values of p, g, gx (g^x where x is private key), and the ASCII text when prompted.

         > **Warning:** It is necessary that _p_ be larger than 130. For example, the prime number 281.

     - ElGamal Decryption Module
       - Run the **_Decrypt.py_** file.
       - Input the values of p, x (private key 1), y (private key 2), and the (c1, c2) pairs when prompted.

     - Encryption and Decryption Module
       - Run the **_Encrypt_Decrypt.py_** file.
       - Input the values of p, g, x, the ASCII text, n (division group for encryption) when prompted.
      
         > **Warning:** In this case, the larger you make _n_, the larger the prime number _p_ will have to be.
         > For example, if we have an n of 3, and the message to be encrypted is "~~~", the prime number has to be larger than 126126126.
> [!TIP]
> You can use the prime number p = 82589933 and its primitive root g = 26 to start.

Good luck! 

from Crypto.Cipher import AES


def resize_length(string):
    #resizes the String to a size divisible by 16 (needed for this Cipher)
    return string.rjust((len(string) // 16 + 1) * 16)

def encrypt(url, cipher):
    # Converts the string to bytes and encodes them with your Cipher
    return cipher.encrypt(resize_length(url).encode())

def decrypt(text, cipher):
    # Converts the string to bytes and decodes them with your Cipher
    return cipher.decrypt(text).decode().lstrip()


# It is important to use 2 ciphers with the same information, else the system breaks (at least for me)
# Define the Cipher with your data (Encryption Key and IV)
cipher1 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
cipher2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
decrypt(encrypt("https://booking.com", cipher1), cipher2)

encrypt("booking.com", cipher1) 
print(cipher1)
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import secrets

backend = default_backend()
iterations = 100_000

def _derive_key(password: bytes, salt: bytes, iterations: int = iterations) -> bytes:
    """Derive a secret key from a given password and salt"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=salt,
        iterations=iterations, backend=backend)
    return b64e(kdf.derive(password))

def password_encrypt(message: bytes, password: str, iterations: int = iterations) -> bytes:
    salt = secrets.token_bytes(16)
    key = _derive_key(password.encode(), salt, iterations)
    return b64e(
        b'%b%b%b' % (
            salt,
            iterations.to_bytes(4, 'big'),
            b64d(Fernet(key).encrypt(message)),
        )
    )

def password_decrypt(token: bytes, password: str) -> bytes:
    decoded = b64d(token)
    salt, iter, token = decoded[:16], decoded[16:20], b64e(decoded[20:])
    iterations = int.from_bytes(iter, 'big')
    key = _derive_key(password.encode(), salt, iterations)
    return Fernet(key).decrypt(token)



#message = 'asd'
#password = 'test1'
#encryptedPassword = password_encrypt(message.encode(), password)
#print(encryptedPassword)
#b'9Ljs-w8IRM3XT1NDBbSBuQABhqCAAAAAAFyJdhiCPXms2vQHO7o81xZJn5r8_PAtro8Qpw48kdKrq4vt-551BCUbcErb_GyYRz8SVsu8hxTXvvKOn9QdewRGDfwx'
#token = '566A64784353633374655A447242716B76734E6C526741426871434141414141414751474F4B646A385038574F3276432D6C4A627648435359714F7642446D344E77546A344B626F6D41395F454C483364474979676F674D5231664367377735586B4A737371316B36316F4A5371363570364953627430754E656D73'
#token2 = bytearray.fromhex(token).decode()
#print(token2)
#decryptedPassword = password_decrypt(token2, password).decode()
#print(decryptedPassword)
#'John Doe'
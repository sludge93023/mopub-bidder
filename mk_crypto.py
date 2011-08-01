from Crypto.Cipher import AES
import base64
import os

BLOCK_SIZE = 16

PADDING = '*'

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

def encodeAES(aes_key, to_encode):
    iv = os.urandom(BLOCK_SIZE)
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    
    data = pad(to_encode)
    encrypted_data = cipher.encrypt(data)
    b64_data = base64.b64encode(encrypted_data)
    
    return iv + b64_data

def decodeAES(aes_key, to_decode):
    iv = to_decode[:BLOCK_SIZE]
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    
    b64_data = base64.b64decode(to_decode[BLOCK_SIZE:])
    decrypted_data = cipher.decrypt(b64_data)
    
    return decrypted_data.rstrip(PADDING)

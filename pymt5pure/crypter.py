from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

from pymt5pure.helpers import hash_password_vrand

PAD_LEN = 16
PAD_STYLE = "pkcs7"


class MT5AES(object):
    def __init__(self, password: str, crypt_rand: str):
        self.crypt_iv = tuple(hash_password_vrand(password, crypt_rand))
        self.aes_key = self.crypt_iv[0] + self.crypt_iv[1]
        self.encrypt_iv = self.crypt_iv[2]
        self.decrypt_iv = self.crypt_iv[3]

        self.crypter = AES.new(self.aes_key, AES.MODE_OFB, self.encrypt_iv)
        self.decrypter = AES.new(self.aes_key, AES.MODE_OFB, self.decrypt_iv)

    def encrypt(self, data):
        padded = pad(data, PAD_LEN, PAD_STYLE)
        return self.crypter.encrypt(padded)[: len(data)]

    def decrypt(self, data):
        padded = pad(data, PAD_LEN, PAD_STYLE)
        return self.decrypter.encrypt(padded)[: len(data)]

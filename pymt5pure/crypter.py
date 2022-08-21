from hashlib import md5

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

PAD_LEN = 16
PAD_STYLE = "pkcs7"


def gen_crypt_rand(crypt_rand):
    # Split to 16-byte pieces
    for i in range(16):
        yield bytes.fromhex(crypt_rand[2 * 16 * i : 2 * 16 * (i + 1)])


def gen_crypt_iv(password, crypt_rand):
    crypt_rand = tuple(gen_crypt_rand(crypt_rand))
    t1 = md5(password.encode("utf-16le")).digest()
    # important - no utf16 between hashes!
    t2 = b"WebAPI"
    r = md5(t1 + t2).digest()
    for i in range(16):
        r = md5(crypt_rand[i] + r).digest()
        yield r


class MT5AES(object):
    def __init__(self, password: str, crypt_rand: str):
        self.crypt_iv = tuple(gen_crypt_iv(password, crypt_rand))
        self.aes_key = self.crypt_iv[0] + self.crypt_iv[1]
        self.encrypt_iv = self.crypt_iv[2]
        self.decrypt_iv = self.crypt_iv[3]

        self.crypter = AES.new(self.aes_key, AES.MODE_OFB, self.encrypt_iv)
        self.decrypter = AES.new(self.aes_key, AES.MODE_OFB, self.decrypt_iv)

    def encrypt(self, data):
        padded = pad(data, PAD_LEN, PAD_STYLE)
        return self.crypter.encrypt(padded)[:len(data)]

    def decrypt(self, data):
        padded = pad(data, PAD_LEN, PAD_STYLE)
        return self.decrypter.encrypt(padded)[:len(data)]

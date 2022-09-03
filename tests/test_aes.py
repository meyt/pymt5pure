from pymt5pure.crypter import MT5AES


def to_bytes(v):
    return bytearray.fromhex(v)


def to_hex(v):
    return v.hex()


def test_aes():
    password = "demoPASWORD^123"
    crypt_rand = (
        "0de18c436abe58fc2517ee949086d588"
        "fca58a6d7fc76a3ff4e6d1f742dd845b"
        "e2d74c1a9b08e418909b15077deb2037"
        "3ef55caf910e207c1cd1e349b25ca230"
        "d2bc83d070a5b7a0f866a482911d449c"
        "9f27c8638bdb82f8c67801b80b5b7e0f"
        "e576778c72fd993b6662e32f5284095e"
        "272416b2f698565cf9c3736cd744de9e"
        "24ee707727785291e1761a344a883625"
        "ded28ec358ac654fbe9a808c9d7e8b88"
        "960cb8b9197fa94b718a90b90192959b"
        "cd1a78bf3c7f777a1ce57240e6714d73"
        "43b99679d07867111e878ee7fe08ec66"
        "fbe41bcd277954851b8c8fb23985eb08"
        "34db51dfd3cd548af1535ce5c954042e"
        "7019c016a302c317c37720071e222fee"
    )
    a = (
        "530059004d0042004f004c005f0054004f00540041004c007c000d000a00",
        "8c6f9e5343b25cd9a902d9f1d17ea99e3317a29f1c2a4bf8e890a954072f",
    )
    b = (
        "530059004d0042004f004c005f0054004f00540041004c007c000d000a00",
        "7b9d6bd126851ae2133dc61c947796afe620e3b07a06027998217d5c7a64",
    )
    aes = MT5AES(password, crypt_rand)
    for i, o in (a, b):
        assert aes.encrypt(to_bytes(i)) == to_bytes(o)

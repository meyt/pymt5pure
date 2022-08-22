from pymt5pure.helpers import hash_password_rand, hash_password_vrand


def test_hash_password_rand():
    r = hash_password_rand(
        password="demoPASWORD^123",
        rand="904ba8ecb16273d2f0ae9c3b8a023752",
    )
    assert r == "280e4b5c1b77289603b9e048b3985058"


def test_hash_password_vrand():
    r = hash_password_vrand(
        password="demoPASWORD^123",
        vrand=(
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
        ),
    )
    assert tuple(r) == (
        b"\x05J,X\x13\xc3\xd7\xe3.}\xa0[\xad{\x11\xb0",
        b"D#%\xe1\xa1\xed\xd3\xf0\\\xf9\x1a\xa5\x89<k\x0b",
        b"\xdaA\xd3\xb5\xca]\xcb\xfeV\xb9\xe5\xe1\xdc\xa8}g",
        b"\x1b\xd1\xd9%a\x8d5$32H\xb2\xc7\x9e\xedr",
        b"P\x13.\x97\x1b8\xa8\\Wg\x19g\x85\xde\x8e\xd9",
        b"k0\xf9\xdd\x06\x8e\xdcH\x89\xc1q]hWU\xbd",
        b"u\xfa\xac\xe9\xc9{5\xe8<\x01\xef\xa5\xf7W\xfc6",
        b"\xb8\xe2\xde\x8c5\xbf\xeb\xca5eG\xaa\xef\xd5\xa4\xff",
        b"\xcd\xa2\x93\x80\x86\xf5z\xc6\xed!\xef\xe2-a\x8e\x13",
        b"\t\x8d\t\xd6\xacw\x9f\x1c\n\xa6T\xb6\x93\xe4\xa3j",
        b"\xde\xaa\x01\x90\xa7\x88\x17\xbb\x1cr\xb9\xa5k+fm",
        b'"o@\xe7,\xf2]*e~\xb6\xb8\x85\x8c\xbd\x8d',
        b"\xd3\xec\x829m\x7f\x93|\x1c\x1433#xj5",
        b"\xd4.F\x18\x9faP\x1c*/z\x91/H\xc8)",
        b"c\xa3;\xa2\xa8f\x82\xfb\xd7\xa6\xd9H_=\xfb\xda",
        b"\n\x1ak\x19\xc5\x8a\xde\x05\x9dp\x9a\xfa\xde\xaa}\xaa",
    )

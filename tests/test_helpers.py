from pymt5pure.helpers import hash_from_password


def test_hash_from_password():
    r = hash_from_password(
        password="demoPASWORD^123",
        srv_rand="904ba8ecb16273d2f0ae9c3b8a023752",
    )
    assert r == "280e4b5c1b77289603b9e048b3985058"

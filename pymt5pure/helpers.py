from os.path import dirname, join
from hashlib import md5

module_dir = dirname(__file__)
package_dir = dirname(module_dir)


def escape(v: str):
    for a, b in (
        ("\\", r"\\\\"),
        ("=", r"\="),
        ("|", r"\|"),
        ("\n", r"\\\n"),
    ):
        v = v.replace(a, b)
    return v


def hash_from_password(password, srv_rand):
    """
    Make SRV_RAND_ANSWER from PASSWORD and SRV_RAND
    """
    t1 = md5(password.encode("utf-16le")).digest()
    t2 = b"WebAPI"  # important - no utf16 between hashes!
    pwd_hash = md5(t1 + t2).digest()
    srv_rand = bytes.fromhex(srv_rand)  # hex string from bytes
    return md5(pwd_hash + srv_rand).hexdigest()


def dump_socket_data(v: bytes, name="response-dump.txt"):  # pragma: nocover
    with open(join(package_dir, name), "wb+") as f:
        f.write(v)

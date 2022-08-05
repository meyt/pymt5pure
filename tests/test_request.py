from pymt5pure.request import Request


def test_body():
    r = Request.format_body("ping")
    assert r == "ping|\r\n"

    r = Request.format_body("ping", dict(a=1))
    assert r == "ping|a=1|\r\n"

    r = Request.format_body("ping", dict(a=1, b="222"))
    assert r == "ping|a=1|b=222|\r\n"


def test_packet():
    r = Request("SYMBOL_NEXT", dict(INDEX=0), num=3).dump()
    assert len(r) == 53
    assert r == b"002c00030" + "SYMBOL_NEXT|INDEX=0|\r\n".encode("utf-16le")

    r = Request("TEST").dump()
    assert len(r) == 23
    assert r == b"000e00000" + "TEST|\r\n".encode("utf-16le")

    r = Request("TEST", num=10).dump()
    assert len(r) == 23
    assert r == b"000e000a0" + "TEST|\r\n".encode("utf-16le")

    r = Request(
        "AUTH_START",
        dict(
            VERSION=3211,
            AGENT="WebApiExtensionExample",
            LOGIN=33007,
            TYPE="MANAGER",
            CRYPT_METHOD="NONE",
        ),
        num=1,
    ).dump()
    assert len(r) == 205
    assert r == (
        b"00c400010"
        + (
            "AUTH_START|VERSION=3211|AGENT=WebApiExtensionExample|"
            "LOGIN=33007|TYPE=MANAGER|CRYPT_METHOD=NONE|\r\n"
        ).encode("utf-16le")
    )

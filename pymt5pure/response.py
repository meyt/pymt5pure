try:
    import ujson as jsonlib
except Exception:
    import json as jsonlib


from pymt5pure.constants import ret_code_map
from pymt5pure.exceptions import ResponseError


def parse_response(data: bytes, data_ext: bytes = None):
    data = data.decode("utf-8")
    fields = data.split("|")
    params = dict()
    for field in fields[1:-1]:
        exploded = field.split("=")
        if len(exploded) == 2:
            k, v = field.split("=")
            params[k.upper()] = v

            if k == "RETCODE":
                status_code, status_text = v.split(" ")
                status_code = int(status_code)
                if status_code != ret_code_map["MT_RET_OK"]:
                    raise ResponseError(v)

        elif field == "\r\n":
            continue

        elif not data_ext:
            data_ext += field

    return dict(
        cmd=fields[0],
        params=params,
        status_code=status_code,
        status_text=status_text,
        binary=data_ext,
    )


class Response:
    def __init__(self, data: bytes):
        self.data = data
        pos = data.find(b"\n")
        self.data_ext = data[pos:]
        fields_str = data[:pos].decode("utf-16le").encode().decode("utf-8")
        fields = fields_str.split("|")
        params = dict()
        for field in fields[1:-1]:
            exploded = field.split("=")
            if len(exploded) == 2:
                k, v = exploded
                params[k.upper()] = v

                if k == "RETCODE":
                    self.status_code, self.status_text = v.split(" ")
                    self.status_code = int(self.status_code)
                    if self.status_code != ret_code_map["MT_RET_OK"]:
                        raise ResponseError(v)

        self.cmd = fields[0]
        self.params = params

    @property
    def json(self):
        if not self.data_ext:
            return

        data = self.data_ext.decode("utf-16le").encode().decode("utf-8")
        return jsonlib.loads(data)

    @property
    def binary(self):
        if not self.data_ext:
            return

        return self.data_ext

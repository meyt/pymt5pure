class MT5Api:
    def __init__(self, client) -> None:
        self.client = client

    def symbol_next(self, pos=0):
        return self.client("SYMBOL_NEXT", INDEX=pos).json

class ParseError(Exception):
    pass


class Parser:
    def __init__(self, s) -> None:
        self.s = s
        self.pos = 0

    def parse(self):
        return self.parse_natural()

    def parse_natural(self):
        res = ""
        # 文字列の大小比較
        if not ("0" <= self.s[self.pos] and self.s[self.pos] <= "9"):
            raise ParseError()
        res += self.s[self.pos]
        self.pos += 1
        if res == "0" and "0" <= self.s[self.pos] and self.s[self.pos] <= "9":
            raise ParseError()
        while self.pos < len(self.s) and "0" <= self.s[self.pos] and self.s[self.pos] <= "9":
            res += self.s[self.pos]
            self.pos += 1
        return int(res)


print(Parser(input()).parse())

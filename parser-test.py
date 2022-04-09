# JSON paser
class ParseError(Exception):
    pass


"""
文字が数字かどうか判定
"""


def is_digit(c):
    # 文字列の大小比較
    return "0" <= c and c <= "9"


class Parser:
    def __init__(self, s) -> None:
        self.s = s
        self.pos = 0

    def parse(self):
        return self.parse_natural()

    def parse_natural(self):
        res = ""
        if not is_digit(self.s[self.pos]):
            raise ParseError()
        res += self.s[self.pos]
        self.pos += 1
        if res == "0" and is_digit(self.s[self.pos]):
            raise ParseError()
        while self.pos < len(self.s) and is_digit(self.s[self.pos]):
            res += self.s[self.pos]
            self.pos += 1
        return int(res)


print(Parser(input()).parse())

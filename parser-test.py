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
        self.spaces()
        x = self.json()
        self.spaces()
        return x

    def json(self):
        c = self.peek()
        if c == "[":
            return self.array()
        return self.parse_natural()

    def spaces(self):
        while True:
            try:
                c = self.peek()
            except ParseError:
                break
            if c == " " or c == "\n" or c == "\t" or c == "\r":
                self.pos += 1
            else:
                break

    def array(self):
        res = []
        c = self.peek()
        if c != "[":
            raise ParseError()
        self.pos += 1
        self.spaces()
        c = self.peek()
        if c == "]":
            self.pos += 1
            return res
        x = self.json()
        res.append(x)
        while True:
            self.spaces()
            c = self.peek()
            if c == "]":
                self.pos += 1
                return res
            if c != ",":
                raise ParseError()
            self.pos += 1
            self.spaces()
            x = self.json()
            res.append(x)

    def parse_natural(self):
        res = ""
        first = self.peek()
        if not is_digit(first):
            raise ParseError()
        res += first
        self.pos += 1
        while True:
            try:
                c = self.peek()
            except ParseError:
                break
            if not is_digit(c):
                break
            if first == "0":
                raise ParseError()
            res += c
            self.pos += 1
        return int(res)

    def peek(self):
        """
        現在位置の文字を返す
        """
        if self.pos < len(self.s):
            return self.s[self.pos]
        else:
            raise ParseError()


print(Parser(input()).parse())

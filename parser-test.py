# JSON paser
from ast import parse


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
        if c == "t" or c == "f":
            return self.boolean()
        if c == "n":
            return self.null()
        if c == "\"":
            return self.string()

        return self.parse_natural()

    def char(self):
        c = self.peek()
        if c == "\"":
            raise ParseError()
        if c == "\\":
            self.pos += 1
            c = self.peek()
            if c == "n":
                self.pos += 1
                return "\n"
            if c == "r":
                self.pos += 1
                return "\r"
            if c == "t":
                self.pos += 1
                return "\t"
            if c == "\\":
                self.pos += 1
                return "\\"
            if c == "\"":
                self.pos += 1
                return "\""
            raise ParseError()
        else:
            self.pos += 1
            return c

    def string(self):
        res = ""
        c = self.peek()
        if not c == "\"":
            raise ParseError()
        self.pos += 1
        while True:
            c = self.peek()
            if c == "\"":
                self.pos += 1
                return res
            x = self.char()
            res += x

    def null(self):
        c = self.peek()
        if not c == "n":
            raise ParseError()
        self.pos += 1
        c = self.peek()
        if not c == "u":
            raise ParseError()
        self.pos += 1
        c = self.peek()
        if not c == "l":
            raise ParseError()
        self.pos += 1
        c = self.peek()
        if not c == "l":
            raise ParseError()
        self.pos += 1

    def boolean(self):
        c = self.peek()
        if c == "t":
            self.pos += 1
            c = self.peek()
            if not c == "r":
                raise ParseError()
            self.pos += 1
            c = self.peek()
            if not c == "u":
                raise ParseError()
            self.pos += 1
            c = self.peek()
            if not c == "e":
                raise ParseError()
            self.pos += 1
            return True

        elif c == "f":
            self.pos += 1
            c = self.peek()
            if not c == "a":
                raise ParseError()
            self.pos += 1
            c = self.peek()
            if not c == "l":
                raise ParseError()
            self.pos += 1
            c = self.peek()
            if not c == "s":
                raise ParseError()
            self.pos += 1
            c = self.peek()
            if not c == "e":
                raise ParseError()
            self.pos += 1
            return False
        else:
            raise ParseError()

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

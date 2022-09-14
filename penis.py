"""
Overengineered Penis Class

No copyright, do whatever you want I am not responsible.
"""

from abc import abstractmethod, ABCMeta

PENIS_HEAD = """
    _____
   /  |  \\
   \\     /
"""
PENIS_BALLS = """
 ____   ____
/    \\ /    \\
\\____/ \\____/
"""


class AbstractPenis(metaclass=ABCMeta):
    """
    Abstract Class Penis

    For implementing various penises
    """

    def __init__(self, length: int) -> None:
        self._length = length

    @property
    @abstractmethod
    def length(self) -> int: pass

    @length.setter
    @abstractmethod
    def length(self, new_length: int): pass

    def shaft(self) -> str:
        return self.length * '   |     |\n'

    def __str__(self) -> str:
        return PENIS_HEAD + self.shaft()[:-1] + PENIS_BALLS


class MeasuredPenis(AbstractPenis):
    """
    MeasuredPenis

    Penis with a length attachment on `__str__`
    """
    @property
    def length(self) -> int:
        return self._length

    @length.setter
    def length(self, new_length: int):
        self._length = new_length

    def shaft(self) -> str:
        buf = ['   |     |'] * self.length
        for (i, segment) in enumerate(buf):
            if i == self.length // 2:
                segment += f'     +--- {self.length} inches'
            elif i == 0:
                segment += ' ----+'
            elif i == self.length - 1:
                segment += ' ----+'
            else:
                segment += '     |'
            buf[i] = segment
        return '\n'.join(buf)


if __name__ == '__main__':
    print(MeasuredPenis(5))

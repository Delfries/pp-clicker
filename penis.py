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

# Penis class


class Penis:
    def __init__(self, length: int) -> None:
        self._length = length

    @property
    def length(self) -> int:
        return self._length

    @length.setter
    def length(self, new_length: int):
        if new_length < 1:
            raise ValueError("Penis length cannot be non-existent or inverted")
        self._length = new_length

    def shaft(self) -> str:
        return self.length * '   |     |\n'

    def __str__(self) -> str:
        return PENIS_HEAD + self.shaft()[:-1] + PENIS_BALLS

class Bitset:

    def __init__(self, size: int):
        self.s = ["0"] * size
        self.f = ["1"] * size
        self.cnt_1 = 0

    def fix(self, idx: int) -> None:
        if self.s[idx] != "1":
            self.s[idx] = "1"
            self.f[idx] = "0"
            self.cnt_1 += 1

    def unfix(self, idx: int) -> None:
        if self.s[idx] != "0":
            self.s[idx] = "0"
            self.f[idx] = "1"
            self.cnt_1 -= 1

    def flip(self) -> None:
        self.s, self.f = self.f, self.s
        self.cnt_1 = len(self.s) - self.cnt_1

    def all(self) -> bool:
        return len(self.s) == self.cnt_1

    def one(self) -> bool:
        return self.cnt_1 > 0

    def count(self) -> int:
        return self.cnt_1

    def toString(self) -> str:
        return "".join(self.s)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
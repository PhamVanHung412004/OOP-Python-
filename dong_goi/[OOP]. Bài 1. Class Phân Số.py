from math import gcd
class Phanso:
    def __init__(self, a : int, b : int) -> None:
        self.a = a
        self.b = b

    def ans(self):
        tmp1 = gcd(self.a, self.b)
        tu = self.a // tmp1
        mau = self.b // tmp1
        print(str(tu) + "/" + str(mau))

a,b = map(int,input().split())


ans = Phanso(a,b)
ans.ans()

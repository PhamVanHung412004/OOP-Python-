# support = {"HT": 2000000,
#            "HP": 900000,
#            "GV": 500000}


# mid = 2
# def check(s : str) -> tuple:
#     return (int(s[mid:]),support[s[ : mid]])

# class infor:
#     def __init__(self,qr : str, heso : int, phucap: int , name : str, luong_co_ban : int) -> None:
#         self.qr = qr
#         self.heso = heso
#         self.phucap = phucap
#         self.name = name
#         self.luong_co_ban = luong_co_ban
#     def print_infor(self) -> None:
#         print(self.qr,self.name,self.heso,str(self.luong_co_ban * self.heso + self.phucap))
# qr = input()
# (he_so,phu_cap) = check(qr)
# print(he_so)
# print(phu_cap)
# name = input()
# luong_co_ban = int(input())
# ans = infor(qr, he_so, phu_cap, name, luong_co_ban)

# ans.print_infor()

class GiaoVien:
    def __init__(self, ma, ten, luong_co_ban):
        self.ma = ma
        self.ten = ten
        self.luong_co_ban = luong_co_ban

    def get_he_so(self):
        return int(self.ma[2:])

    def get_thu_nhap(self):
        he_so = self.get_he_so()
        luong = he_so * self.luong_co_ban
        cv = self.ma[0:2]
        if cv == 'HT':
            return luong + 2000000
        elif cv == 'HP':
            return luong + 900000
        else:
            return luong + 500000

    def __str__(self):
        return f'{self.ma} {self.ten} {self.get_he_so()} {self.get_thu_nhap()}'

if __name__ == '__main__':
    g = GiaoVien(input(), input(), int(input()))
    print(g)

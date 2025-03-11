class Nhanvien:
    def __init__(self, name : str, luong : int, ngay : int, rank : str) -> None:
        self.name = name
        self.luong = luong
        self.ngay = ngay
        self.rank = rank

    def print_ans(self):
        thuong = 0
        if (self.ngay < 22):
            thuong = 0
        elif (22 <= self.ngay < 25):
            thuong += int(0.1 * self.luong)
        else:
            thuong += int(0.2 * self.luong)

        total = self.ngay * self.luong

        phucap = 0
        if (self.rank == "GD"):
            phucap += 250000
        elif (self.rank == "PGD"):
            phucap += 200000
        elif (self.rank == "TP"):
            phucap += 180000
        else:
            phucap += 150000
        print("NV01",self.name,int(total),int(thuong),int(phucap),int((total + thuong + phucap)))


ans = Nhanvien(input(),int(input()),int(input()),input())
ans.print_ans()

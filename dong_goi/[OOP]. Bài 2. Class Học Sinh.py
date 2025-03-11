class infor:
    def __init__(self, name : str, birth_day : str, toan : float, ly : float, hoa : float) -> None:
        self.name = name
        self.birth_day = birth_day
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
    def print_infor(self) -> None:
        age = self.toan + self.ly + self.hoa 
        ans = "{:.1f}".format(age)
        print(self.name,self.birth_day,str(ans))

name = input()
birth_day = input()
toan = float(input())
ly = float(input())
hoa = float(input())

ans = infor(name,birth_day,toan,ly,hoa)
ans.print_infor()
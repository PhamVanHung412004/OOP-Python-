class Time:
    def __init__(self, usename : str, Pass : str, name : str, time_in : str, time_out : str) -> None: 
        self.usename = usename
        self.Pass = Pass
        self.name = name
        self.time_in = time_in
        self.time_out = time_out

    def get_gio_choi(self):
        h1,m1 = int(self.time_in[0 : 2]), int(self.time_in[3 : ])
        h2,m2 = int(self.time_out[0 : 2]), int(self.time_out[3 : ])
        time1 = h1 * 60 + m1
        time2 = h2 * 60 + m2
        return time2 - time1
    
    def get_username(self):
        return self.usename
    
    def __str__(self):
        phut_choi = self.get_gio_choi()
        h = phut_choi // 60
        m = phut_choi % 60
        return f"{self.usename} {self.Pass} {self.name} {h} gio {m} phut"
def main():
    n = int(input())
    a  = []
    for i in range(n):
        s = Time(input(), input(), input(), input(), input())
        a.append(s)
    a.sort(key = lambda x : (-x.get_gio_choi(),x.get_username()))
    for i in a:
        print(i)
main()
from functools import cmp_to_key
class Student:
    def __init__(self,ID : str,name : str, arr_score : list) -> None:
        self.ID = format(ID,"02d")
        self.ID = "HS" + self.ID
        self.name = name
        self.arr_score = arr_score[::]
    
    def calc_AVB(self) -> float:
        return sum(self.arr_score) / len(self.arr_score)
    def check_score(self) -> str:
        dtb = self.calc_AVB()
        if (dtb >= 9):
            return "XUAT SAC"
        elif (dtb >= 8):
            return "GIOI"
        elif (dtb >= 7):
            return "KHA"
        elif (dtb >= 5):
            return "TB"
        else:
            return "YEU"
    def get_ID(self):
        return int(self.ID[2 : ])
    def print_ans(self):
        print(self.ID,self.name,"{:.1f}".format(self.calc_AVB()),self.check_score())
def cmp(a : Student, b : Student) -> int:
    tb1 = a.calc_AVB()
    tb2 = b.calc_AVB()
    if (tb1 != tb2):
        if (tb1 > tb2):
            return -1
        else:
            return 1
    else:
        ma1 = a.get_ID()
        ma2 = b.get_ID()
        if (ma1 < ma2):
            return -1
        else:
            return 1

def main():
    t = int(input())
    arr_information = []
    for i in range(t):
        student = Student(i + 1,input(),list(map(float,input().split())))
        arr_information.append(student)
    arr_information.sort(key=cmp_to_key(cmp))
    for i in arr_information:
        i.print_ans()
main()

class Student:
    def __init__(self,ID : str ,name : str, cls : str , gmail : str) -> None:
        self.ID = ID
        self.name = name
        self.cls = cls
        self.gmail = gmail
    def print_ans(self):
        print(self.ID, self.name,self.cls,self.gmail)
def main() -> None:
    t = int(input())
    arr_information = []
    for i in range(t):
        student = Student(input(), input(), input(), input())
        arr_information.append(student)
    arr_information.sort(key=lambda x : x.cls, reverse=False)
    for i in arr_information:
        i.print_ans()
main()
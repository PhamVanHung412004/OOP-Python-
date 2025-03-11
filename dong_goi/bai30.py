from sys import stdin
class Student:
    def __init__(self, ID : str, name : str, cls : str, gmail : str) -> None:
        self.ID = ID
        self.name = name
        self.cls = cls
        self.gmail = gmail

    def get_ID(self) -> str:
        return self.ID
        
    def print_ans(self):
        print(self.ID,self.name, self.cls, self.gmail)

def main():
    line = []
    for x in stdin:
        line.append(x[:-1])
    # print(line)
    a = []
    for i in range(0,len(line),4):
        student = Student(line[i],line[i + 1],line[i + 2],line[i + 3])
        a.append(student)
    a.sort(key = lambda x : x.get_ID())
    for i in a:
        i.print_ans()
main()


def get_name_new(name : str) -> str:
    name_split = name.split()
    for i in range(len(name_split)):
        name_split[i] = name_split[i].lower()

    for i in range(len(name_split)):
        name_split[i] = name_split[i].capitalize()

    name_new = ""
    for i in name_split:
        name_new += i + " "
    return name_new[: -1]
class Student:
    def __init__(self, ID : str, name : str, cls : str, gmail : str) -> None:
        self.ID = ID
        self.name = name
        self.cls = cls
        self.gmail = gmail
    def format_name(self) -> str:
        return get_name_new(self.name)
    def __str__(self):
        return f"{self.ID} {self.format_name()} {self.cls} {self.gmail}"
def main():
    n = int(input())
    arr = []
    for i in range(n):
        s = Student(input(), input(), input(), input())
        arr.append(s)
    Q = int(input())
    
    for i in range(Q):
        s = input()
        print("DANH SACH SINH VIEN LOP",s,":")
        for j in arr:
            if (s == j.cls):
                print(j)

main()
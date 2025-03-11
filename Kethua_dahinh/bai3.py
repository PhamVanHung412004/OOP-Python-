def string_new(birth_day) -> str:
    arr_string = birth_day.split("/")
    if (len(arr_string[0]) == 1):
        arr_string[0] = "0" + arr_string[0]
    if (len(arr_string[1] )== 1):
        arr_string[1] = "0" + arr_string[1]
    res = ""
    arr_string.insert(1,"/")
    arr_string.insert(3,"/")
    for i in arr_string:
        res += i
    return res

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

class INIT:
    def __init__(self, ID : str, name : str, ngay_sinh : str, add : str, cls : str, GPA : float) -> None:
        self.ID : str = ID 
        self.name : str = name 
        self.ngay_sinh : str = ngay_sinh 
        self.add : str = add 
        self.cls : str = cls 
        self.GPA : float = GPA 
    def __str__(self):
        if (self.ID[: 2] == "SV"):
            GPA_new = format(self.GPA, ".2f")
            return f"{self.ID} {get_name_new(self.name)} {string_new(self.ngay_sinh)} {self.add} {self.cls} {GPA_new}"
        else:
            return f"{self.ID} {get_name_new(self.name)} {string_new(self.ngay_sinh)} {self.add} {self.cls} {int(self.GPA)}"

class Informatin_Peason(INIT):
    def __init__(self,ID : str, name : str, ngay_sinh : str, add : str, cls : str, GPA : float) -> None:
        super().__init__(ID, name, ngay_sinh, add, cls, GPA)
    def get_name(self) -> str:
        return self.name

def main():
    n = int(input())
    list_students = []
    list_teacher = []
    for i in range(n):
        ID = input()
        infor = Informatin_Peason(ID, input(), input(), input(), input(), float(input()))

        if (ID[ : 2] == "SV"):
            list_students.append(infor)
        else:
            list_teacher.append(infor)
    if (len(list_teacher) != 0):
        print("DANH SACH GIAO VIEN :")
        for i in list_teacher:
            print(i)
    if (len(list_students) != 0):
        print("DANH SACH SINH VIEN :")
        for i in list_students:
            print(i)

main()
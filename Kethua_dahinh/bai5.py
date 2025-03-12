from functools import cmp_to_key

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


class Information:
    def __init__(self, ID : str, name : str, birth_day : str, add : str, cls : str, money : float) -> None:
        self.ID : str = ID
        self.name : str = get_name_new(name)
        self.birth_day : str = string_new(birth_day)
        self.add : str = add
        self.cls : str = cls
        self.money : float = money

class Student(Information):
    def __init__(self, ID : str, name : str, birth_day : str, add : str, cls : str, money : float) -> None:
        super().__init__(ID, name, birth_day, add, cls, money)

    def get_ID_class_student(self) -> str:
        return self.ID

    def get_GPA(self) -> float:
        return self.money

    def __str__(self) -> None:
        GPA = self.money
        GPA = "{:.2f}".format(GPA)
        return f"{self.ID} {self.name} {self.birth_day} {self.add} {self.cls} {GPA}"

class Teacher(Information):
    def __init__(self, ID : str, name : str, birth_day : str, add : str, cls : str, money : float) -> None:
        super().__init__(ID, name, birth_day, add, cls, money)
    
    def get_ID_class_teacher(self) -> str:
        return self.ID

    def get_Money(self) -> int:
        return int(self.money)

    def __str__(self) -> None:
        return f"{self.ID} {self.name} {self.birth_day} {self.add} {self.cls} {int(self.money)}"


def print_ans(value_check : str, arr : list[Student : Teacher]) -> None:
    for i in arr:
        if (i.ID[: 2] == value_check):
            print(i)
def main():
    n = int(input())
    list_teachers = []
    list_students = []
    for i in range(n):
        ID_infor = input()
        if (ID_infor[ : 2] == "GV"):
            Information_Teacher = Teacher(ID_infor, input(), input(), input(), input(), float(input()))   
            list_teachers.append(Information_Teacher)
        else:
            Information_Student = Student(ID_infor, input(), input(), input(), input(), float(input()))   
            list_students.append(Information_Student)
 
    # name_add = input()
    print("DANH SACH GIAO VIEN :")
    list_teachers.sort(key=lambda x : (-x.get_Money(),x.get_ID_class_teacher()))
    for i in list_teachers:
        print(i)
    
    print("DANH SACH SINH VIEN :")
    list_students.sort(key=lambda x : (-x.get_GPA(),x.get_ID_class_student()))
    for i in list_students:
        print(i)
main()

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
    def __init__(self, ID : str, name : str, birth_day : str, add : str, group : str, money : float, cls : str) -> None:
        self.ID : str = ID
        self.name : str = get_name_new(name)
        self.birth_day : str = string_new(birth_day)
        self.add : str = add
        self.group : str = group
        self.money : int = money
        self.cls : str = cls
    
    def get_add(self) -> str:
        return self.add

class Student(Information):
    def __init__(self, ID : str, name : str, birth_day : str, add : str, group : str, money : float, cls : str = None) -> None:
        super().__init__(ID, name, birth_day, add, group, money, cls)

    def __str__(self) -> None:
        GPA = self.money
        GPA = "{:.2f}".format(GPA)
        return f"{self.ID} {self.name} {self.birth_day} {self.add} {self.group} {GPA}"

class Teacher(Information):
    def __init__(self, ID : str, name : str, birth_day : str, add : str, group : str, money : float, cls : str) -> None:
        super().__init__(ID, name, birth_day, add, group, money, cls)

    def __str__(self) -> None:
        return f"{self.ID} {self.name} {self.birth_day} {self.add} {self.group} {int(self.money)}"

def print_ans(value_check : str,arr : list[Student : Teacher] = None) -> None:
    for i in arr:
        if (i.get_add() == value_check):
            print(i)
def main():
    n = int(input())
    list_teachers = []
    list_students = []
    for i in range(n):
        ID_infor = input()
        if (ID_infor[ : 2] == "GV"):
            infor = Teacher(ID_infor, input(), input(), input(), input(), float(input()), input())   
            list_teachers.append(infor)
        else:
            infor1 = Student(ID_infor, input(), input(), input(), input(), float(input()), None)   
            list_students.append(infor1)

    name_add = input()
    print("DANH SACH GIAO VIEN CO DIA CHI TAI {} : ".format(name_add))
    print_ans(name_add,list_teachers)
    print("DANH SACH SINH VIEN CO DIA CHI TAI {} : ".format(name_add))
    print_ans(name_add,list_students)

main()

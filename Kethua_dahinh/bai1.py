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

class Person:
    def __init__(self, name: str, ngay_sinh: str, diachi: str) -> None:
        self.name:str = name
        self.ngay_sinh:str = ngay_sinh
        self.diachi:str = diachi

    def Tostring(self) -> str:
        return get_name_new(self.name) + " " + string_new(self.ngay_sinh) + " " + self.diachi


class Student(Person):
    def __init__(self, name : str, ngay_sinh : str, diachi : str, cls : str, GPA : float) -> None:
        super().__init__(name, ngay_sinh, diachi)
        self.cls : str = cls
        self.GPA: float = format(GPA, ".2f")

    def Tostring(self) -> str:
    	return " " + self.cls + " " + str(self.GPA)

def main():
    n = int(input())
    for i in range(n):
        ID = str(i + 1)
        while(len(ID) < 4):
            ID = "0" + ID

        name = input()
        birth_day = input()
        add = input()
        information_person = Person(name, birth_day, add)
        information_student = Student(name,birth_day, add, input(), float(input()))
        result = ID + " " + information_person.Tostring() + information_student.Tostring()
        print(result)
        # information_students.Tostring()
        # print(ID,information_person.Tostring() + information_students.Tostring())
main()

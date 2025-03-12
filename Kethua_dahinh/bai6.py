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

class Infor:
	def __init__(self,ID : str, name : str, birth_day : str, add: str,  cls : str) -> None:
		self.ID: str = ID
		self.name: str = get_name_new(name)
		self.birth_day: str = string_new(birth_day)
		self.add: str = add
		self.cls: str = cls


class Teacher(Infor):
	def __init__(self,ID : str, name : str, birth_day : str, add: str,  cls : str, money : int, name_class : str) -> None:
		Infor.__init__(self,ID, name, birth_day, add, cls) 
		self.money: int = money
		self.name_class: str = name_class	

	def __str__(self):
		return f"{self.ID} {self.name} {self.birth_day} {self.add} {self.cls} {self.money} {self.name_class}"

class Student(Infor):
	def __init__(self,ID : str, name : str, birth_day : str, add: str,  cls : str, GPA : int) -> None:
		Infor.__init__(self,ID, name, birth_day, add, cls) 
		self.GPA: float = format(GPA, ".2f")

	def __str__(self):
		return f"{self.ID} {self.name} {self.birth_day} {self.add} {self.cls} {self.GPA}"


def main():
	n = int(input())
	list_teachers = []
	list_students = []
	for i in range(n):
		ID = input()
		if (ID[: 2] == "GV"):
			information_teacher = Teacher(ID, input(), input(), input(), input(), int(input()), input())
			list_teachers.append(information_teacher)
		else:
			information_student = Student(ID, input(), input(), input(), input(), float(input()))
			list_students.append(information_student)

	name_class_check = input()

	print("DANH SACH GIAO VIEN PHU TRACH LOP {} :".format(name_class_check))
	for i in list_teachers:
		if (i.name_class == name_class_check):
			print(i)
		# if (i.name_class == name_class_check):

		# 	print(i)
	print("DANH SACH SINH VIEN LOP {} :".format(name_class_check))
	for i in list_students:
		if (i.cls == name_class_check):
			print(i)

main()


'''
SV2
Vu AnH MaNH
13/10/2004
Ha Noi
DTVT1
2.70

GV1
Nguyen VAn TuaN
6/2/1975
Nam Dinh
DTVT
25000000
CNTT1	
'''

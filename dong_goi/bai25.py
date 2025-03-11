
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
class Student:
    def __init__(self, ID : str, name : str, sex : str, birth_day : str, add : str, number : str, day : str) -> None:
        self.ID = ID
        self.name = name
        self.sex = sex
        self.birth_day = birth_day
        self.add = add
        self.number = number
        self.day = day

    def format_birth_day(self) -> str:
        return string_new(self.birth_day)
    def format_day(self) -> str:
        return string_new(self.day)
    def print_ans(self):
        print(self.ID, self.name, self.sex, self.format_birth_day(),self.add,self.number,self.format_day())

def main():
    n = int(input())
    for i in range(n):
        ID = str(i + 1)
        while(len(ID) < 5):
            ID = "0" + ID
        studens = Student(ID,input(),input(),input(),input(),input(), input())
        studens.print_ans()
main()
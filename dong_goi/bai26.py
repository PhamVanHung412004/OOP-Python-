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
def get_information(arr : list, index : int) -> int:
   return arr[index]

class Student:
    def __init__(self, ID : str, name : str, sex : str, birth_day : str, add : str, number : str, day : str) -> None:
        self.ID = ID
        self.name = name
        self.sex = sex
        self.birth_day = birth_day
        self.add = add
        self.number = number
        self.day = day

    def split_day_birth(self) -> list:
        splits = list(map(int,self.birth_day.split("/")))
        return splits
        
    def format_birth_day(self) -> str:
        return string_new(self.birth_day)

    def format_day(self) -> str:
        return string_new(self.day)

    def get_year(self):
        return self.split_day_birth()[2]

    def get_month(self):
        return self.split_day_birth()[1]

    def get_day(self):
        return self.split_day_birth()[0]

    def print_ans(self):
        print(self.ID, self.name, self.sex, self.format_birth_day(),self.add,self.number,self.format_day())

def main():
    n = int(input())
    arr_information = []
    for i in range(n):
        ID = str(i + 1)
        while(len(ID) < 5):
            ID = "0" + ID
        studens = Student(ID,input(),input(),input(),input(),input(), input())
        arr_information.append(studens)
    arr_information.sort(key=lambda x : (x.get_year(),x.get_month(),x.get_day()),reverse=False)
    for i in arr_information:
    #     print(i.get_year())
        i.print_ans()
main()
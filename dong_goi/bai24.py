class Studetn:
    def __init__(self, ID : str, name : str, cls : str, birth_day : str, GPA : float) -> None:
        self.ID = ID
        self.name = name
        self.cls = cls
        self.birth_day = birth_day
        self.GPA = "{:.2f}".format(GPA)

    def format_birth_day(self) -> str:
        s = self.birth_day
        arr_string = self.birth_day.split("/")
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

    def format_name_lower(self):
        Name = self.name
        name_lower = Name.lower()
        name_lower = name_lower.split(" ")
        for i in range(len(name_lower)):
            name_lower[i] = name_lower[i].capitalize()    
        name_last = ""
        for i in range(len(name_lower)):
            name_last += name_lower[i] + " "        
        return name_last[ : len(name_last) - 1]
    def print_ans(self):
        print(self.ID, self.format_name_lower(), self.cls,self.format_birth_day(),self.GPA)
def main():
    n = int(input())
    arr_information_students = []
    for i in range(n):
        ID = str(i + 1)
        while(len(ID) < 3):
            ID = "0" + ID
        ID = "SV" + ID
        student = Studetn(ID,input(), input(),input(), float(input()))    
        arr_information_students.append(student)
    arr_information_students.sort(key=lambda x : x.GPA,reverse=True)
    for i in arr_information_students:
        i.print_ans()
main()  
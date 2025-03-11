def format(s : str) -> list:
    return [s[i] for i in range(len(s)) if (s[i] == '/')]
class Students:
    def __init__(self,ID : str ,name : str, cls : str, birth_day : str, GPA : float) -> None:
        self.ID = ID
        self.name = name
        self.cls = cls
        self.birth_day = birth_day
        self.GPA = GPA
    
    def format_name(self):
        full_name = self.name.split(" ")
        name_new = ""
        for i in range(len(full_name)):
            full_name[i] = full_name[i].capitalize()
            name_new += full_name[i] + " "
        return name_new[ : len(name_new) - 1]

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

    def print_ans(self):
        print(self.ID,self.format_name(),self.cls,self.format_birth_day(),self.GPA)

def main():
    t = int(input())
    list_ans = []
    for i in range(t):  
        digit = str(i + 1)
        while(len(digit) < 3):
            digit = "0" + str(digit)
        digit = "SV" + digit
        information = Students(digit,input(), input(), input(),"{:.2f}".format(float(input())))
        information.print_ans()
        # ans = information
        # list_ans.append(ans)
    
    # for i in list_ans:
    #     print(i)
main()

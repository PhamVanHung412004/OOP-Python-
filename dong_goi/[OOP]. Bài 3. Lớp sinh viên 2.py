def tranform(s : str) -> str:
    index_string = []
    split_s = s.split("/")
    index_s = [i for i in range(len(split_s)) if (len(split_s[i]) == 1)]
    
    for i in range(len(s)):
        if (s[i] == '/'):
            t = i - 1
            cnt = 0
            s_tranform_new = ""
            while(s[t] != '/' and t >= 0):
                cnt += 1
                s_tranform_new += s[t]
                t -= 1
            if (len(s_tranform_new) == 1):
                s_tranform_new = '0' + s_tranform_new
                index_string.append(s_tranform_new)

    for i in range(len(index_s)):
        split_s[index_s[i]] = index_string[i]
    s_new = ""
    cnt = 0
    for i in range(len(split_s)):
        s_new += split_s[i]
        s_new += '/'
        cnt += 1
        if (cnt == 2):
            break
    s_new += split_s[-1]
    return s_new

def init(s : str) -> str:
    index = s.index('.')
    ans = s[ : index + 1]
    ans += s[index + 1: index + 2]
    return ans


class infor:
    def __init__(self, msv : str,name : str, khoa : str, birth_day : str, gpa : str) -> None:
        self.msv = msv
        self.name = name
        self.khoa = khoa
        self.birth_day = birth_day
        self.gpa = gpa

    def print_infor(self):
        print(self.msv,self.name,self.khoa,self.birth_day,self.gpa)
name = input()
khoa = input()
birth_day = input()
birth_day = tranform(birth_day)
gpa = input()
gpa = init(gpa)

ans = infor("SV001",name,khoa,birth_day,gpa)
ans.print_infor()
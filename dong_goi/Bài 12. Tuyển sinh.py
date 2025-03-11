# # class Infor:
# #     def __init__(self,  ma : str, name : str, math : float, ly : float, hoa : float) -> None:
# #         self.ma = ma
# #         self.name = name
# #         self.math = math
# #         self.ly = ly
# #         self.hoa = hoa

# def list_kv() -> dict:
#     ans = {
#         "KV1" : 0.5,
#         "KV2" : 1,
#         "KV3" : 2.5 ,
#     }
#     return ans



# class Sinhvien:
#     def __init__(self, ma : str, name : str, math : float, ly : float, hoa : float) -> None:
#         self.ma = ma
#         self.name = name
#         self.math = math
#         self.ly = ly
#         self.hoa = hoa
#     def print_ans(self):
#         value = list_kv()
#         scorce_ss = value[self.ma[ : len(self.ma) - 1]]

#         total_S = self.math + self.ly + self.hoa + scorce_ss
#         total_S = "{:.1f}".format(total_S)
#         tmp = str(total_S)
#         index = tmp.index(".")
#         oke = False
#         if (tmp[index + 1: ] == "0"):
#             oke = True

#         if (oke):
#             total_S = int(total_S)
#         s = ""
#         if (float(total_S) < 24.0):
#             s += "TRUOT"
#         else:
#             s += "TRUNG TUYEN"
#         print(self.ma,self.name,self.ma[2: len(self.ma) - 1],str(total_S),s)



# ma = input()
# name = input()
# math = float(input())
# ly = float(input())
# hoa = float(input())

# ans = Sinhvien(ma, name, math, ly, hoa)
# ans.print_ans()


class Sinhvien:
    def __init__(self, khuvuc : str, name : str, toan : float, ly : float, hoa : float) -> None:
        self.khuvuc = khuvuc
        self.name = name
        self.toan = toan
        self.ly = ly
        self.hoa = hoa

    def print_ans(self):
        total = self.toan + self.hoa + self.ly
        check_kv = self.khuvuc
        if (check_kv[:3] == "KV1"):
            total += 0.5
        elif (check_kv[: 3] == "KV2"):
            total += 1
        else:
            total += 2.5
        
        check_total = str(total)
        index_zero = check_total.index(".")
        if (check_total[index_zero + 1: ] == "0"):
            total = int(total)
        else:
            total = "{:.1f}".format(total)
        
        result = ""
        if (float(total) < 24):
            result += "TRUOT"
        else:
            result += "TRUNG TUYEN"
        print(self.khuvuc,self.name,check_kv[ : 3][-1],total,result)


kv = input()
name = input()
toan = float(input())
ly = float(input())
hoa = float(input())

ans = Sinhvien(kv, name, toan, ly, hoa)

ans.print_ans()

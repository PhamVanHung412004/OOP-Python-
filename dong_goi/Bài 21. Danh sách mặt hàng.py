
class Mathang:
    def __init__(self,ma,ten, don_vi, gia_mua, gia_ban):
        self.ma = ma
        self.ten = ten
        self.don_vi = don_vi
        self.gia_ban = gia_ban
        self.gia_mua = gia_mua
    def get_loi_nhuan(self):
        return self.gia_ban - self.gia_mua
    def print_ans(self):
        print(self.ma,self.ten,self.don_vi,self.gia_mua,self.gia_ban,self.gia_ban - self.gia_mua)
    # def __str__(self):
    #     return f"{self.ma}{" "}{self.ten}{" "}{self.don_vi  }{" "}{self.gia_mua}{" "}{self.gia_ban}{" "}{self.gia_ban - self.gia_mua}"


# def Binary_Search()


n = int(input())

list_infor = []
list_set = set()
arrs = []
for i in range(n):
    digit = str(i + 1)
    # name = "MH" + str(i + 1)
    while(len(digit) < 4):
        digit = "0" + digit
    information = Mathang("MH" + digit,input(),input(),int(input()), int(input()))
    arrs.append(information)
    # price = information.gia_ban - information.gia_mua
    # list_set.add(price)
    # list_infor.append([price, i + 1])
arrs.sort(key=lambda x : -x.get_loi_nhuan())
for i in range(len(arrs)):
    arrs[i].print_ans()
# list_set = list(list_set)
# list_infor.sort(reverse=True)

# for i in range(len(list_set)):
#     l = int(1e7)
#     r = 0
#     for j in range(len(list_infor)):
#         if (list_set[i] == list_infor[j][0]):
#             l = min(l,j)
#             r = max(r,j)
#     arr = []
#     index = []
#     for j in range(l,r + 1):
#         arr.append([list_infor[j][1],list_infor[j][0]])
#         index.append(j)
#     arr.sort()
#     for j in range(len(arr)):
#         list_infor[index[j]] = [arr[j][1],arr[j][0]]


# for i in range(len(list_infor)):
#     ma = "MH000" + str(list_infor[i][1])
#     self_ma = Binary_Search(arrs,ma)
#     # for j in range(len(arrs)):
#     #     pointer = arrs[j]
#     #     self_ma = pointer.ma
#     #     if (list_infor[i][1] == int(self_ma[5 :])):
#     #         pointer.print_ans()

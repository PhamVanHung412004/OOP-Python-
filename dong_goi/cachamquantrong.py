

#Các hàm phổ biến trong lập trình
# init : khởi tạo trường thông tin
# hàm hủy __del__: vai trò hàm hủy sẽ xóa tham chiêú tới object
# chú ý: trong python có cơ chế tự dọn nên không cần dùng hàm __del__
# ham __str__: hàm in ra thông tin của một đối tượng nếu không dùng hàm __str__ thì nó sẽ hiển thị ra địa chỉ của class
# Eg1:
# class Person:
#     def __init__(self, name, birth):
#         self.name = name
#         self.birth = birth


# if __name__ == '__main__':
#     s = Person("Hung", 21)
#     print(s)


# class Person:
#     def __init__(self, name, birth):
#         self.name = name
#         self.birth = birth
#     def __str__(self):
#         return f'{self.name}{self.birth}'

# if __name__ == '__main__':
#     s = Person("Hung", 21)
#     print(s)


# Ham __repr__: Trả về chuỗi kí tự đại diện cho một đối tượng nếu bạn không cài đặt hàm __repr__
#Eg:
class Information:
    def __init__(self, name, bitrh):
        self.name = name
        self.bitrh = bitrh


if __name__ == '__main__':
    infor = Information("Hung", 21)
    print(infor)
    print(infor.__repr__)

'''
d4umoctxi5
'''
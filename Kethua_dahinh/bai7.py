class Information:
	def __init__(self,ID : str, name : str, title : str, color : str, V :int, price : int) -> None:
		self.ID: str = ID
		self.name: str = name
		self.title: str = title
		self.color: str = color
		self.V: int = V
		self.price: int = price


class Car(Information):
	def __init__(self,ID : str, name : str, title : str, color : str, V : int, price : int) -> None:
		Information.__init__(self,ID ,name, title, color, V, price)

	def __str__(self):
		return f"{self.ID} {self.name} {self.title} {self.color} {self.V} {self.price}"

class Motorbike(Information):
	def __init__(self,ID : str, name : str, title : str, color : str, V : int, price : int) -> None:
		Information.__init__(self, ID, name, title, color, V, price)

	def __str__(self):
		return f"{self.ID} {self.name} {self.title} {self.color} {self.V} {self.price}"

def main():
	n = int(input())
	list_Cars = []
	list_Motorbikes = []
	for i in range(n):
		name = input()
		if (name[ : 3] == "OTO"):
			information_car = Car(name, input(), input(),input(),int(input()),int(input()))
			list_Cars.append(information_car)	
		else:
			information_motorbike = Motorbike(name, input(), input(),input(),int(input()),int(input()))
			list_Motorbikes.append(information_motorbike)


	name_check = input()
	print("DANH SACH XE HANG {} :".format(name_check))
	for i in list_Cars:
		if (i.title == name_check):
			print(i)

	for i in list_Motorbikes:
		if (i.title == name_check):
			print(i)

main()

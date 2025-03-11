
class Nhanvien:
    def __init__(self, name : str, luong : int, songaycong : int, chucvu : str) -> None:
        self.name = name
        self.luong = luong
        self.songaycong = songaycong
        self.chucvu = chucvu
    def res(self):
      ans = 0
      if (self.chucvu == "GD"):
        ans += 25000
      elif (self.chucvu == "PGD"):
        ans += 200000 
      elif (self.chucvu == "TP"):
        ans += 18000
      else:
        ans += 15000
      res = 0
      if (22 <= self.songaycong < 25):
        res += 0.1 * self.luong
      elif (self.songaycong >= 25):
        res += 0.2 * self.luong
      print("NV01",self.name,res,ans,)
      

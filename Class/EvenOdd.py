class Number:
 def __init__(self, num):
  self.num = num

 def check(self):
   if self.num % 2 == 0:
     print("Even Number")
   else:
     print("Odd Number")

n = Number(10)
n.check()
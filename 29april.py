n = int(input())
a = 1900
b = 3000
a <= n <= b
if not n%100==0 and n%4==0 or n%400==0:
  print("Високосный")
else:
  print("Обычный")

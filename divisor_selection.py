def reg(n):
  j = 0
  i = 2
  while i**2<=n and j!=1:
    if n % i == 0:
      j = 1
    else: 
      i = i + 1
  else:
    if j == 1:
      j = "Составное число"
    elif j == 0:
      j = "Простое число"
  return j

n = int(input())
print(reg(n))

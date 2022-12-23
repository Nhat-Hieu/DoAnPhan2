#2.2
from sympy import *

def tinh_gioi_han():
  x = symbols('x')
  f = (x**1/3*sqrt(x**3-3*x*2) + sqrt(x*2 - 2*x))
  answer = limit(f, x, oo)
  print('Kết quả giới hạn: ', answer)
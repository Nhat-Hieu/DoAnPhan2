#2.3
from sympy import *

def tinh_dao_ham():
  x = symbols('x')
  f = (2*x-1)/(x+2)
 #Tính đạo hàm df/dx
  answer = diff(f, x)
  print("Kết quả đạo hàm là:",answer)

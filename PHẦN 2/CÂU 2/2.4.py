#2.4
from sympy import *

def tinh_nguyen_ham():
  x = symbols('x')
  f = x/(x**2+1)
  answer = integrate(f, x)
  print("Kết quả nguyên hàm là: ", answer)
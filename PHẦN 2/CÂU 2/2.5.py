#2.5
from sympy import *

def tich_phan():
#Mô tả biến
  x = symbols('x')
#Xây dựng hàm
  f = ((1-x*tan(x))/(x*x*cos(x)+x))
#Tính tích phân có giới hạn
  answer = integrate(f, (x,(2*pi/3),pi))
  print("Kết quả tích phân là: ", answer)
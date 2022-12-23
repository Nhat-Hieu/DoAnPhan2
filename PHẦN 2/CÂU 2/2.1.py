#2.1
from sympy import symbols, Eq, solve

def he_phuong_trinh():
  x, y, z = symbols('x y z')
#Hệ phương trình
  eq1 = Eq(2*x - 5*y + z,-5)
  eq2 = Eq(4*x + 2*y - 2*z, 2)
  eq3 = Eq(x + y - z, 0)
  answer = solve((eq1, eq2, eq3), (x,y,z))
  print('Nghiệm của hệ phương trình là: ', answer)

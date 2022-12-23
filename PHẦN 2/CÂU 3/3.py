import numpy as np
from sympy import *
import matplotlib.pyplot as plt

def ham_bac_4(a,b,c,d,e,x):
  y = x*x*x*x - 2*x*x - 3
  return y

x = np.linspace(start=-10.0,stop=10.0, num=200)
y = ham_bac_4(1,0, -2, 0,-3, x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Đồ thị phương trình y")
ax.set_xlabel("Trục hoành - x")
ax.set_ylabel("Trục tung - y")
plt.show()

#y đạo hàm
x = symbols('x')
y = x*x*x*x - 2*x*x - 3
y_1phay = diff(y,x)
print(y_1phay)

def ham_bac_3(a,b,c,d,x):
  y_1phay = 4*x**3 - 4*x
  return y_1phay

x = np.linspace(start=-10.0,stop=10.0, num=200)
y_1phay = ham_bac_3(4,0,-4,0,x)
fig, ax = plt.subplots()
ax.plot(x, y_1phay)
ax.set_title("Đồ thị phương trình y 1 phẩy")
ax.set_xlabel("Trục hoành - x")
ax.set_ylabel("Trục tung - y_1phay")
plt.show()

#y' đạo hàm
x = symbols('x')
y_1phay = 4*x**3 - 4*x
y_2phay = diff(y_1phay,x)
print(y_2phay)

def ham_bac_2(a,b,c,x):
  y_2phay = 12*x**2 - 4
  return y_2phay

x = np.linspace(start=-10.0,stop=10.0, num=200)

y_2phay = ham_bac_2(12,0,-4,x)
fig, ax = plt.subplots()
ax.plot(x, y_2phay)
ax.set_title("Đồ thị phương trình y 2 phẩy")
ax.set_xlabel("Trục hoành - x")
ax.set_ylabel("Trục tung - y_2phay")
plt.show()

#đạo hàm của y''
x = symbols('x')
y_2phay = 12*x**2 - 4
y_3phay = diff(y_2phay,x)
print(y_3phay)

def ham_bac_1(a,b,x):
  y_3phay = 24*x
  return y_3phay

x = np.linspace(-10,10,200)

y_3phay = ham_bac_1(24,0,x)
fig, ax = plt.subplots()
ax.plot(x, y_3phay)
ax.set_title("Đồ thị phương trình y 3 phẩy")
ax.set_xlabel("Trục hoành - x")
ax.set_ylabel("Trục tung - y_3phay")
plt.show()
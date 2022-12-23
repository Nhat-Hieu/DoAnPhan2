import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def ve_mat_yen_ngua(z):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')

  # Tạo mảng giá trị x và y
  x = y = np.arange(-5, 5, 0.5)
  X, Y = np.meshgrid(x, y)

  # Tính giá trị z
  Z = (X/3)**2 - (Y/2)**2

  # Vẽ đồ thị
  ax.plot_surface(X, Y, Z)
  plt.show()

#Vẽ với giá trị z là 1
ve_mat_yen_ngua(1)


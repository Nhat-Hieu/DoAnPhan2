import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def hyperbolic():
    # Tạo mảng dữ liệu theo trục x, y
    x, y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))

    # Tính toán giá trị theo trục z
    z = (((x/3)**2 + (y/5)**2 - 1)**(1/2))*2

    # Tạo đối tượng 3D axes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Vẽ đồ thị
    ax.plot_surface(x, y, z, alpha=0.5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

hyperbolic()
plt.show()



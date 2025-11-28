
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import seaborn as sb
plt.rcParams['figure.dpi'] = 200
theta = np.linspace(0, 2*np.pi, 20)
x = np.linspace(0, 2, 20)
X, T = np.meshgrid(x, theta)
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
# fig, ax = plt.subplots()
xx = 4*np.cos(T)
yy = 4 * np.sin(T)
zz = X
ax.plot_surface(xx, yy, zz, alpha=0.5, cmap='viridis',
                linewidth=0.5, antialiased=True)

x = np.linspace(0, 4, 100)

z = np.sqrt(x)
y = np.full_like(x, 0)
ax.plot(x, y, z, alpha=0.5)
ax.set_aspect('equal')
ax.fill_between(x, y, y, x, y, z)

X, T = np.meshgrid(x, theta)
yy = X*np.cos(T)
zz = np.sqrt(X)
xx = X*np.sin(T)

ax.plot_surface(xx, yy, zz, alpha=0.5, cmap='plasma',
                linewidth=0.5, antialiased=True)
plt.show()

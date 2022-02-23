import numpy as np
import matplotlib.pyplot as plt

x = [0.5, 11.5, 16, 17, 30]
y = [2.1, 6.82,8.68, 10.54, 11.9]
plt.errorbar(x, y, xerr=0.5, yerr=0.5)
p, v = np.polyfit(x, y, deg=1, cov=True)

print(np.polyfit(x, y, deg=1, cov=False))
plt.grid()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01)
sp=plt.subplot(111)
sp.plot(x, x*x-x-6)

sp.spines['right'].set_position('center')
sp.spines['left'].set_position('center')
sp.spines['top'].set_position('center')
sp.spines['bottom'].set_position('center')
plt.axis('equal')
plt.show()
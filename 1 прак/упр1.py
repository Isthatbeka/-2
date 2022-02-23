import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.01)
sp=plt.subplot(111)
sp.plot(x, np.log((np.exp(1/(np.sin(x)+1))/((5/4)+(1/5*x**1))/np.log(1+x**2))))
sp.spines['right'].set_position('center')
sp.spines['left'].set_position('center')
sp.spines['top'].set_position('center')
sp.spines['bottom'].set_position('center')

plt.show()